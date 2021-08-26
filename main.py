from vuilen_getlink import get_api_json, get_post_ep, full_decode_flow

import time



from flask import Flask, request # Import Flask Class
app = Flask(__name__) # Create an Instance



@app.route('/') # Route the Function
def main(): # Run the function
	return """
  <b>Bước 1</b>: Cài HLS player (còn gọi là m3u8 player) bằng plugin vào trình duyệt <br>
    <a href="https://chrome.google.com/webstore/detail/hls-player-m3u8-streaming/eakdijdofmnclopcffkkgmndadhbjgka">Chrome Plugin</a>
  <br><br>
  <b>Bước 2</b>: Nhập link vào thanh địa chỉ của trình duyệt theo cú pháp  https://vuighe-getlink.ttpro1995.repl.co/vuighe/get?link='link cua ban'. 
  <br><br>
  ví dụ <br>
  https://vuighe-getlink.ttpro1995.repl.co/vuighe/get?link=https://vuighe.net/majo-no-tabitabi/tap-1
  <br><br>
  
  <b>Bước 3</b>: Chờ khá lâu (không refresh, không F5), tầm 5 giây (thay vì 30 giây xem quảng cáo). Bạn sẽ thấy trình duyệt có 1 link duy nhất. Click vào link đó, Chrome sẽ phát video. Nếu video không phát mà download thì xem Bước 1, và tắt IDM nếu có. 

  <br><br> Không có quảng cáo <br>
  Toàn bộ mã nguồn:  https://github.com/ttpro1995/vuighe-getlink
  """


@app.route('/vuighe/get')
def getlink_direct():
  
  link = request.args.get('link', default="nope" ,type = str)
  if link=="nope":
    print("Nhap link vao ban oi, vi du https://getlink-endpoint.ttpro1995.repl.co/fshare/get?link=https://www.fshare.vn/file/ACNYKM94HTE8QOX")
  output_link = full_decode_flow(link)
  html = """
  <a href="output_link">output_link</a>
  """
  result = html.replace("output_link", output_link)
  return result



app.run(host='0.0.0.0', port=5000, debug=False) # Run the Application (in 
