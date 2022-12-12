from flask import Flask,render_template,jsonify,request
import processor

app=Flask(__name__)

app.config['SECCRET_KEY']= 'enter-a-very-secretive-key-3819373'


@app.route('/',methods=["GET"])
def index():
    return render_template('indexes.html',**locals())


@app.route('/chatbot',methods=["POST"])
def  chatbotResponse():
    if request.method == 'POST':
        the_question = request.form['question']

        response = processor.chatbot_response(the_question)

    return jsonify({"response":response})


if __name__ == '__main__':
 app.run(host='0.0.0.0',port='8080',debug=True)
