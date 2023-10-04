from flask import Blueprint, render_template, request, flash, redirect

#internal imports
from Capstone_site.models import Pet, User, db # product_schema, products_schema
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
        desc = createform.description.data
        image = createform.image.data
        birthday = createform.birthday.data

        community = Pet(name, birthday, image, desc) 

        db.session.add(community)
        db.session.commit()

        flash(f"You have successfully added your pet {name}", category='success')
        return redirect('/')

        # except:
        #     flash("We were unable to process your request. Please try again", category='warning')
        #     return redirect('/shop/create')
        
    return render_template('create.html', form=createform)

#create our first route
@site.route('/')
def community():

    # make the api call here 
    # make a func in helpers and call it here 

    community = Pet.query.all()
    users = User.query.all()

    index_stats = {
        'pets in community': len(community),
        'users' : len(users)
    }

    return render_template('index.html', stats=index_stats) # put in variable for the api call 





#create our CREATE route
@site.route('/index/update/<id>', methods = ['GET', 'POST'])
def update(id):

    updateform = PetForm()
    pet = Pet.query.get(id) #WHERE clause WHERE product.prod_id == id 

    if request.method == 'POST' and updateform.validate_on_submit():

        try: 
            pet.name = updateform.name.data
            pet.description = updateform.description.data
            pet.set_image(updateform.image.data, updateform.name.data) #calling upon that set_image method to set our image!
            pet.birthday = updateform.birthday.data

            

            db.session.commit() #commits the changes to our objects 

            flash(f"You have successfully updated product {pet.name}", category='success')
            return redirect('/')

        except:
            flash("We were unable to process your request. Please try again", category='warning')
            return redirect('/index/update')
        
    return render_template('update.html', form=updateform, pet=pet)

@site.route('/index/delete/<id>')
def delete(id):

    pet = Pet.query.get(id)

    db.session.delete(pet)
    db.session.commit()

    return redirect('/')

