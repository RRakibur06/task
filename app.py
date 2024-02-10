from flask import Flask, render_template, request 

app = Flask(__name__, template_folder='templates') 

@app.route('/') 
def index():
    return render_template('form.html') 


@app.route('/resume', methods=['POST']) 
def calculate():
    image = request.form['image']
    name = request.form['name'] 
    post = request.form['post'] 
    email = request.form['email']
    address = request.form['address']
    skills = request.form['skills']
    certification_one = request.form['certification_one']
    certification_two = request.form['certification_two']
    organization_name = request.form['organization_name']
    position = request.form['position']
    edu_duration = request.form['edu_duration']
    experience = request.form['experience'] 
    edu_organization_name = request.form['edu_organization_name']
    degree = request.form['degree']
    duration = request.form['duration']
    project_name_one = request.form['project_name_one']
    project_details_one = request.form['project_details_one']
    project_name_two = request.form['project_name_two']
    project_details_two = request.form['project_details_two']
    project_name_three = request.form['project_name_three']
    project_details_three = request.form['project_details_three']
    return render_template('resume.html',image=image,name=name,post=post,email=email,address=address,skills=skills,certification_one=certification_one,certification_two=certification_two,
     organization_name=organization_name,position=position,duration=duration,experience=experience,
     edu_organization_name=edu_organization_name,degree=degree,edu_duration=edu_duration,
     project_name_one=project_name_one,project_details_one=project_details_one,                    
     project_name_two=project_name_two,project_details_two=project_details_two,                    
     project_name_three=project_name_three,project_details_three=project_details_three,                    
    ) 


if __name__ == '__main__':
    app.run(debug=True)