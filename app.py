from flask import Flask , render_template , request , redirect ,send_file
import openpyxl
import pandas as pd
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/data" , methods=['GET','POST'])
def data():
    req_cols = ["Item Name" ,"Seller SKU","Unit Price","Variation"]
    if request.method == "POST":
        csv = request.files['file']
        if csv:
            df_new = pd.read_csv(csv,sep=';',encoding='utf-8',usecols=req_cols)
            # Color Column
            color = df_new['Variation'].str.split(',' ,expand=True)[0]
            df_new['Color'] = color.str.split(':' , expand=True)[1]
            # Size Column
            size = df_new['Variation'].str.split(',' ,expand=True)[1]
            df_new['Size'] = size.str.split(':' ,expand=True)[2]
            del df_new['Variation']
            # Get Ready stock product
            df_new = df_new[df_new["Seller SKU"].str.contains("MTHPOS|mthpos|MJGMP|mjgmp|pl00|PL00|mjtj|MJTJ|CL00|cl00") == True]
            # Insert data
            df_new.insert(1, "PTY" , "Daraz")
            # Changing headers name
            df_after_rename = df_new.rename(columns={"Item Name": "Design Name","Seller SKU": "Code"})
            write_excel_file = pd.ExcelWriter('data.xlsx')
            df_after_rename.to_excel(write_excel_file,index=False)
            write_excel_file.save()
        return redirect('/download')
@app.route('/download')
def downloadFile():
    download_path = "data.xlsx"
    return send_file(download_path, as_attachment=True)
if __name__ == '__main__':
    app.run(debug=True) 
