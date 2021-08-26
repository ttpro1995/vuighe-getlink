import requests
import json
import re


def get_post_ep(url_raw):
  """
  Read html to find value of data-id and data-episode-id
  """
  html = requests.get(url_raw)

  regex_pattern_step1 = r'(data-id=".*?" data-video-id=)|(data-episode-id=".*?")'
  regex_pattern_step2 = r'".*?"'
  match = re.findall(regex_pattern_step1, html.text)

  # get data_id 
  match_data_id = re.search(regex_pattern_step2, match[0][0])
  data_id = match_data_id.group(0)

  # match ep id 
  match_ep_id = re.search(regex_pattern_step2, match[1][1])
  ep_id = match_ep_id.group(0)

  return data_id, ep_id

def get_api_json(data_id, ep_id, url_raw):
  """
  Call vuighe api 
  """
  # discard double quote "
  data_id = data_id.strip('\"')
  ep_id = ep_id.strip('\"')

  # build api url
  url = 'https://vuighe.net/api/v2/films/'+data_id+'/episodes/'+ ep_id
  header = {
  "Referer":url_raw,
  'Content-Type': 'application/json',
  'X-Requested-With': 'XMLHttpRequest',
  }
  result = requests.get(url, headers=header)
  print(url)
  return result.json();


def decode_m3u8_hash(hash):
  """
  The m3u8 link is encrypt, we need to decrypt and build m3u8 url.
  The result m3u8 url can be play with any m3u8 player
  """
  # example input: -1156\x7fjj( 5-,($+-k&*(j-)6j'!w!qv!&}qwtrt'$|w!v'r&v'! |r&vq$!q!}ttuj5)$<),61k(v0}
  result = ""
  for i in range(len(hash)):
    # get unicode value of string at position i
    o = ord(hash[i])

    # and with 69 
    r = o ^ 69 

    decode_char = chr(r)
    result+= decode_char
  
  # result is https://mephimanh.com/hls/bd2d43dc842171ba92d3b7c3bde97c34ad4d8110/playlist.m3u8 
  # but we need to extract the code bd2d43dc842171ba92d3b7c3bde97c34ad4d8110
  # and build new url with domain ima21 
  # "https://ima21.xyz/hls/bd2d43dc842171ba92d3b7c3bde97c34ad4d8110/playlist.m3u8"

  # get the code from link 
  m3u8_code = result.split("/")[4]

  # build new link with the code
  result_link = "https://ima21.xyz/hls/" + m3u8_code + "/playlist.m3u8"
  return result_link

def full_decode_flow(vuighe_link):
  # read html to find post id and ep id 
  data_id, ep_id = get_post_ep(vuighe_link)
  # call api for m3u8 link
  resp_json = get_api_json(data_id, ep_id, vuighe_link)
  # decrypt the m3u8 link
  m3u8_encrypt = resp_json["sources"]["m3u8"]["hdp"]
  m3u8_link = decode_m3u8_hash(m3u8_encrypt)
  return m3u8_link

