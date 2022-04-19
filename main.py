from flask import Flask, request, render_template

app = Flask(__name__)

#reyneerperez@gmail.com
@app.route('/', methods=["POST"])

def list_numbers():
    """
    DESCRIPTION: This function interprets the template 'pares_impares.html' values
    ​​and returns a dictionary indicating which numbers are odd or even.
    
    RETURN: render_template("pares_impares.html")
    """
    if request.method=="POST":
        arg  = request.form.get("numbers")
        
        arg = arg.split(",")
        
        arg = list(map(int,arg))


        arg.sort()  

        pares = []
        impares = []   
         
        for i in arg:
          if i % 2 == 0:
            pares.append(i)
          elif i % 2 != 0:
            impares.append(i)
          else:
            None 
        
        dic = {
            "Números pares": pares,
            "Números impares": impares,
        }

        return render_template("pares_impares.html", dic=dic)
    
    return render_template("pares_impares.html")



