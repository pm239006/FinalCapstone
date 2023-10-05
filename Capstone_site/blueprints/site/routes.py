from flask import Blueprint, render_template, request, flash, redirect

#internal imports
from Capstone_site.models import Pet, PetSchema, User, db, pet_schema, pets_schema
from Capstone_site.forms import PetForm



#we need to instantiate our Blueprint objectf
site = Blueprint('site', __name__, template_folder='site_templates') #telling your blueprint where to load the html files 



#create our CREATE route
@site.route('/index/create', methods = ['GET', 'POST'])
def create():

    createform = PetForm()

    if request.method == 'POST' and createform.validate_on_submit():

        # try: 
        name = createform.pet_name.data 
        age = createform.age.data
        birthday = createform.birthday.data
        breed = createform.birthday.data
        fur_color = createform.fur_color.data
        gender = createform.gender.data
        home_trained = createform.home_trained.data 
 
        pets = Pet(name, age,  birthday, breed, fur_color, gender, home_trained)
       

        db.session.add(pets)
        db.session.commit()

        flash(f"You have successfully added {name}", category='success')
        return redirect('/')

        # except:
        #     flash("We were unable to process your request. Please try again", category='warning')
        #     return redirect('/shop/create')
        
    return render_template('create.html', form=createform)

#create our display all pets route
@site.route('/')
def community():
    pets = Pet.query.all()
    users = User.query.all()

    return render_template('index.html',pets=pets) # put in variable for the api call 


@site.route('/resources')
def resources():

    return render_template('resources.html')


#create our UPDATE route
@site.route('/index/update/<id>', methods = ['GET', 'POST'])
def update(id):

    updateform = PetForm()
    pets = Pet.query.get(id) #WHERE clause WHERE product.prod_id == id 

    if request.method == 'POST' and updateform.validate_on_submit():

        try: 

            pet_name = updateform.pet_name.data 
            pet_age = updateform.age.data
            pet_birthday = updateform.birthday.data
            pet_breed = updateform.breed.data
            pet_fur_color = updateform.fur_color.data
            pet_gender = updateform.gender.data
            pet_home_trained = updateform.home_trained.data
        
            db.session.commit() #commits the changes to our objects 

            flash(f"You have successfully updated product {PetSchema.name}", category='success')
            return redirect('/')

        except:
            flash("We were unable to process your request. Please try again", category='warning')
            return redirect('/index/update')
        
    return render_template('update.html', form=updateform)

@site.route('/index/delete/<id>')
def delete(id):

    pet = Pet.query.get(id)

    db.session.delete(pet)
    db.session.commit()

    return redirect('/')


# @site.route('/upload', methods=['POST'])
# def upload():
#   form = UploadForm(request.form)
#   if form.validate():
#     image = form.image.data
#     filename = image.filename
#     image.save('/path/to/images/' + filename)

#     new_image = Image(name=form.name.data, image=image)
#     db.session.add(new_image)
#     db.session.commit()

#     return redirect('/')
