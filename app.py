from flask import Flask,redirect,render_template as render,url_for,request,send_file,Response
from lsb import txt2img,bits2ascii,decode
from lsb3 import txt2img3,bits2ascii3,decode3
from noise import txt2imgv,img2bitsv,bits2txtv,generate_video,get_frames
from PIL import Image
from io import BytesIO,StringIO
app=Flask(__name__)



'''1 channel'''
@app.route('/',methods=['GET','POST'])
def landing():
    return render('landing.html')

@app.route('/encrypt',methods=['GET'])
def encrypt():
    return render('encryption.html')

@app.route('/download/encrypted',methods=['POST'])
def downloadencrypt():
    if request.method=='POST':
        text=request.form['text']
        img=request.files['img']
        output_img = txt2img(text, img)
        img_io = BytesIO()
        output_img.save(img_io,'png',quality=100)
        img_io.seek(0)
        return send_file(img_io, attachment_filename='hidden_text.png', as_attachment=True)
    return render('master.html')

@app.route('/decrypt',methods=['GET'])
def decrypt():
    return render('decryption.html')

@app.route('/download/decrypted',methods=['POST'])
def downloaddecrypt():
    if request.method=='POST':
        img=request.files['img']
        bits=decode(img)
        s=bits2ascii(bits)
        with open('output.txt', 'w') as f:
            f.write(s)
        return send_file('output.txt', as_attachment=True)
    return render('master.html')



'''3 channel'''
@app.route('/encrypt3',methods=['GET'])
def encrypt3():
    return render('encryption3.html')

@app.route('/download/encrypted3',methods=['POST'])
def downloadencrypt3():
    if request.method=='POST':
        text=request.form['text']
        img=request.files['img']
        output_img = txt2img3(text, img)
        img_io = BytesIO()
        output_img.save(img_io,'png',quality=100)
        img_io.seek(0)
        return send_file(img_io, attachment_filename='hidden_text.png', as_attachment=True)
    return render('master.html')

@app.route('/decrypt3',methods=['GET'])
def decrypt3():
    return render('decryption3.html')

@app.route('/download/decrypted3',methods=['POST'])
def downloaddecrypt3():
    if request.method=='POST':
        img=request.files['img']
        bits=decode3(img)
        s=bits2ascii3(bits)
        with open('output.txt', 'w') as f:
            f.write(s)
        return send_file('output.txt', as_attachment=True)
    return render('master.html')



'''to vid'''
@app.route('/encryptv',methods=['GET'])
def encryptv():
    return render('encryptionv.html')

@app.route('/download/encryptedv',methods=['POST'])
def downloadencryptv():
    if request.method=='POST':
        text=request.form['text']
        n=txt2imgv(text)
        generate_video()
        video_path = 'output.avi'
        return send_file(video_path, as_attachment=True)
    return render('master.html')

@app.route('/decryptv',methods=['GET'])
def decryptv():
    return render('decryptionv.html')

@app.route('/download/decryptedv',methods=['POST'])
def downloaddecryptv():
    if request.method=='POST':
        vid=request.files['vid']
        vid.save('vid/' + vid.filename)
        frames=get_frames(vid.filename,30)
        bits=''
        for i in frames:
            bits=bits+img2bitsv(i)
        s=bits2txtv(bits)
        with open('output.txt',mode='w', encoding='utf-8') as f:
            f.write(s)
        return send_file('output.txt', as_attachment=True)
    return render('master.html')



if __name__=='__main__':
    app.run(debug=True)