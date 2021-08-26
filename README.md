Giải thích nguyên lý hoạt động: 

Bây giờ, bạn có link sau 
https://vuighe.net/majo-no-tabitabi/tap-1 

Để lấy được link anime coi quảng cáo, thì mình làm các bước sau 

# Tìm data-id và data-episode-id

Có thể hiểu: data-id chỉ bộ anime, còn data-episode-id chỉ tập mấy. Mình sẽ đọc html từ link https://vuighe.net/majo-no-tabitabi/tap-1  để tìm. 

Trong html, bạn sẽ thấy đoạn sau: 

    <div class="container play" data-id="6031" data-video-id="" data-episode-id="140305" data-episode-name="40"
Đây, data-id="6031", data-episode-id="140305"


# Gọi vuighe api 

Với data-id="6031", data-episode-id="140305", gọi api vào link này 

  https://vuighe.net/api/v2/films/6031/episodes/140305

Nhưng bạn phải đặt lại header: 

    header = {
    "Referer":https://vuighe.net/majo-no-tabitabi/tap-1,
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    }

Lưu ý, ở mục Referer phải để cái link ban đầu, tức là link https://vuighe.net/majo-no-tabitabi/tap-1

Sau khi gọi api, bạn sẽ được json như sau 


    {
      "id": 140243,
      "name": 1,
      "special_name": 0,
      "detail_name": "Toki wo Koeru Omoi",
      "full_name": "Tập 1 - Toki wo Koeru Omoi",
      "film_name": "InuYasha Movie",
      "slug": "tap-1-toki-wo-koeru-omoi",
      "link": "/inuyasha-movie/tap-1-toki-wo-koeru-omoi",
      "views": 2594,
      "is_copyrighted": 0,
      "has_preview": 0,
      "thumbnail_small": "https://s199.imacdn.com/vg/2021/07/23/7d2e439f3e1d3f09_e6656ba9b166c62d_56910162704054179674.jpg",
      "thumbnail_medium": "https://s199.imacdn.com/vg/2021/07/23/7d2e439f3e1d3f09_e6656ba9b166c62d_56910162704054179674.jpg",
      "upcoming": null,
      "midroll": 600,
      "midroll2": 1200,
      "server": -1,
      "sources": {
        "vip": [
          {
            "src": "https://s100.imacdn.com/vg/2021/07/23/6752_140243.mp4?hash=EvFncc1Ivz1CnYFa19oJvg&expire=1630017191&title=InuYasha Movie Tập 1 - Toki wo Koeru Omoi (480p)",
            "type": "video/mp4",
            "quality": "480p"
          }
        ],
        "gd": [],
        "pt": [],
        "yt": [],
        "fb": [
          {
            "src": "https://scontent-lga3-1.xx.fbcdn.net/v/t66.36240-6/10000000_567769627748247_5715546957165878869_n.mp4?_nc_cat=102&ccb=1-5&_nc_sid=985c63&efg=eyJybHIiOjE5MzIsInJsYSI6NDA5NiwidmVuY29kZV90YWciOiJvZXBfaGQifQ%3D%3D&_nc_ohc=fz9EkpXncuMAX81MnwA&rl=1932&vabr=1288&_nc_ht=scontent-lga3-1.xx&edm=APRAPSkEAAAA&oh=39aaae115d8e9571b94b264903b44bcc&oe=612911DF",
            "type": "video/mp4",
            "quality": "720p"
          }
        ],
        "embed": null,
        "mp4": null,
        "m3u8": {
          "hdp": "-1156jj( 5-,($+-k&*(j-)6jv|vvs'p!p!v}u'}&}|r!w''#'w|||#}prswu&#prj5)$<),61k(v0}"
        }
      },
      "meta": {
        "ads": {
          "midroll": {
            "data": [
              {
                "skip": 15,
                "backup": "https://pubads.g.doubleclick.net/gampad/ads?correlator=[timestamp]&iu=/21697904207/vuighe.net_prerollmobile&env=vp&gdfp_req=1&output=vast&sz=640x480&description_url=http%3A%2F%2Fvuighe.net&tfcd=0&npa=0&vpmute=0&vpa=0&vad_format=linear&url=http%3A%2F%2Fvuighe.net&vpos=preroll&unviewed_position_start=1",
                "url": "https://delivery.yomedia.vn/vast?pid=9337c0f2291d4dbfb9a9769a79996634&ec=0",
                "link": null
              },
              {
                "skip": 5,
                "backup": null,
                "url": "https://imad24.com/www/vast/zone/1",
                "link": null
              }
            ]
          },
          "preroll": {
            "data": [
              {
                "skip": 5,
                "backup": null,
                "url": "https://imad24.com/www/vast/zone/1",
                "link": null
              },
              {
                "skip": 15,
                "backup": "https://pubads.g.doubleclick.net/gampad/ads?correlator=[timestamp]&iu=/21697904207/vuighe.net_prerollmobile&env=vp&gdfp_req=1&output=vast&sz=640x480&description_url=http%3A%2F%2Fvuighe.net&tfcd=0&npa=0&vpmute=0&vpa=0&vad_format=linear&url=http%3A%2F%2Fvuighe.net&vpos=preroll&unviewed_position_start=1",
                "url": "https://delivery.yomedia.vn/vast?pid=9337c0f2291d4dbfb9a9769a79996634&ec=0",
                "link": null
              },
              {
                "skip": 15,
                "backup": "https://delivery.lavanetwork.net//www/delivery/fc.php?script=bannerTypeHtml:vastInlineBannerTypeHtml:vastInlineHtmlExtend&format=vast&nz=1&zones=pre-roll%3D1966&version=2",
                "url": "https://blueadss.com/zKVtNgsj1F7oR-v3KH53fsW77QM_CSm48PRf3F93KjNaxI7HNcSFce9Tka347RjFJcSGXWUE2IsxV6OH9dlLn4me4gIdOz3I",
                "link": null
              }
            ]
          },
          "pause": []
        },
        "next": {
          "id": 140501,
          "name": 2
        },
        "previous": null,
        "ago": 33,
        "country": "vn"
      }
    }

# Lấy link m3u8

Ở json ở bước trên, các bạn để ý chỗ `sources`, `m3u8`, `hdp`


    "sources": {
      "vip": [
        {
          "src": "https://s100.imacdn.com/vg/2021/07/23/6752_140243.mp4?hash=EvFncc1Ivz1CnYFa19oJvg&expire=1630017191&title=InuYasha Movie Tập 1 - Toki wo Koeru Omoi (480p)",
          "type": "video/mp4",
          "quality": "480p"
        }
      ],
      "gd": [],
      "pt": [],
      "yt": [],
      "fb": [
        {
          "src": "https://scontent-lga3-1.xx.fbcdn.net/v/t66.36240-6/10000000_567769627748247_5715546957165878869_n.mp4?_nc_cat=102&ccb=1-5&_nc_sid=985c63&efg=eyJybHIiOjE5MzIsInJsYSI6NDA5NiwidmVuY29kZV90YWciOiJvZXBfaGQifQ%3D%3D&_nc_ohc=fz9EkpXncuMAX81MnwA&rl=1932&vabr=1288&_nc_ht=scontent-lga3-1.xx&edm=APRAPSkEAAAA&oh=39aaae115d8e9571b94b264903b44bcc&oe=612911DF",
          "type": "video/mp4",
          "quality": "720p"
        }
      ],
      "embed": null,
      "mp4": null,
      "m3u8": {
        "hdp": "-1156jj( 5-,($+-k&*(j-)6jv|vvs'p!p!v}u'}&}|r!w''#'w|||#}prswu&#prj5)$<),61k(v0}"
      }
    },

Đó chính là những gì ta cần. Nhưng mà nó đang được mã hóa: 

    -1156jj( 5-,($+-k&*(j-)6jv|vvs'p!p!v}u'}&}|r!w''#'w|||#}prswu&#prj5)$<),61k(v0}

Bạn giải mã bằng cách biến nó thành số trong bảng mã unicode, rồi XOR (dấu ^) với 69.

    result = ""
    for i in range(len(hash)):
      # get unicode value of string at position i
      o = ord(hash[i])

      # and with 69 
      r = o ^ 69 

      decode_char = chr(r)
      result+= decode_char

Sau khi giải mã, bạn được link như sau 
https://mephimanh.com/hls/bd2d43dc842171ba92d3b7c3bde97c34ad4d8110/playlist.m3u8
Bạn tách bd2d43dc842171ba92d3b7c3bde97c34ad4d8110 ra, rồi tạo link mới: 
https://ima21.xyz/hls/bd2d43dc842171ba92d3b7c3bde97c34ad4d8110/playlist.m3u8

# Player
https://ima21.xyz/hls/bd2d43dc842171ba92d3b7c3bde97c34ad4d8110/playlist.m3u8 

Bạn cần tìm hls player(vd: https://www.hlsplayer.org/), còn gọi là m3u8 player, rồi bỏ link ấy vào.

Mình khuyên bạn cài luôn cái chrome extension xài cho tiện. 
https://chrome.google.com/webstore/detail/hls-player-m3u8-streaming/eakdijdofmnclopcffkkgmndadhbjgka

