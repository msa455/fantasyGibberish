# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 19:47:46 2019

@author: sam
"""

from flask import Flask, request, render_template
import jaconv


app = Flask(__name__)

katakana_chart = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヽヾ"
hiragana_chart = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖゝゞ" 
hir2kat = str.maketrans(hiragana_chart, katakana_chart)
kat2hir = str.maketrans(katakana_chart, hiragana_chart)



@app.route('/gibberish')
def gibberish():
    return render_template("index.html")

@app.route("/gibberish", methods=["POST"])
def gibberish_post():
    text = request.form['userInput']
    kana = jaconv.alphabet2kana(text)
    kana = list(kana)
    temp = ""
    for char in kana:
        if char in hiragana_chart:
            char = char.translate(hir2kat)
        temp += char
        temp += ","
    return temp.strip(",")

if __name__ == '__main__':
    app.run(debug=True)
    
    