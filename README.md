
<img src="https://i.imgur.com/CYJCaua.png" alt="website">

### Code Institute Milestone Project 3

# **Chocolatier** 


An all-chocolate website where users can contribute recipes and get recommendations for essential baking tools. 

<img src="https://i.imgur.com/b9sdn9o.jpg" alt="banner">

## UX 

### User stories

As a user, I would like to:
- create, read, edit and delete recipes.
- to buy baking tools recommended by the recipes.


As a seller, I would like to: 

- showcase my products alongside baking recipes
- sell baking tools to a target audience.

### Mockup

Since the main goal of this project is to create, read, edit and delete records from the Mongodb database, I did a basic design so the user can easily manouver around the website and to manipulate the data. I did as much as possible gave each route a separate page and a confirmation message that a submission and deletion of entry was made.

[Mobile wireframes](https://i.imgur.com/un7WiC3.png)

[Desktop wireframes](https://i.imgur.com/ew0vM1t.png)

## Features 

### Existing Features
- Sidenavbar - For mobile view, users can navigate the website through the sidenavbar or the links in the footer.
- Uniform cards - Users will have great ease scanning for reipes because of the uniformity of the layout of the recipe cards.
- Page updates - Users are redirected to updated pages upon submission, revision or deletion of a recipe. 
- Form validation - Users will not be allowed to submit a form if a field is left blank or if the required input type is not met.
- Modals - Modals are used to confirm a submission or deletion of a recipe. During deletions, users can choose to either confirm and will be directed back to the updated All Recipes page or to cancel. During revisions, users are given a confirmation message that their recipe has been added.
- Randomized product recommendation - A random product will be recommended upon opening a whole recipe. I made this by using 

    ```products=mongo.db.products.aggregate([{'$sample': {'size': 3}}])```

    to randomly get 3 products from the collection. Then use Jinja for and if loop to pick one from the 3 products. Otherwise, Jinja will throw a "TypeError: object of type 'Cursor' has no len()".

    ````
        {% for product in products %}
        {% if loop.index < 2 %}
        {% endif %}
        {% endfor %}
    ````
### Future Features
- User login - This project did not require a user login that is why I did not include it. Although, it would be optimal for websites like this to have a user login so not anyone can edit and delete data. This project is mainly for CRUD operations.
- Search option - I did not include a search option because my website is already narrowed down to one subject, CHOCOLATE, and the products I included were baking products mostly used with chocolates. A search option right now would be unnecessary.
- Product page - I did not include a product page because I want to focus on the CRUD operations for the recipes. The products were secondary.

## Technologies Used ##

Here are the list of programming languages, technologies, libraries, frameworks and plugin used for this website:

- HTML
- CSS
- [Bootstrap](https://getbootstrap.com/) - used for navbars, grid, parallax, buttons, forms and card styling
- [MaterializeCSS](https://materializecss.com/) - used for additional styling and components like textarea and Modals
- [Google Fonts](https://fonts.google.com/) - used for font-styles [Playfair](https://fonts.google.com/specimen/Playfair+Display?query=playfair), [Merriweather](https://fonts.google.com/specimen/Merriweather?query=merriweather), [Roboto](https://fonts.google.com/specimen/Roboto?query=roboto)
- [Font Awesome](https://fontawesome.com/) - used for icons
- [jQUery](https://jquery.com/) - used for eventhandling and animation 
- [Jquery Validate Plugin](https://jqueryvalidation.org/) - a jquery plugin used for form validation
- [Python 3.8.2](https://www.python.org/) - used for building a connection between Mongodb database and Flask app
- [Flask](https://pypi.org/project/Flask/) - used as the project's framework, Flask uses dependencies and store them in ````requirements.txt```` to build environments.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - used for handling templates
- [MongoDb Atlas](https://www.mongodb.com/cloud/atlas) - MongoDB cloud service used for making document database that stores JSON-like documents
- [Heroku](https://www.heroku.com/home) - used for hosting this project. Github cannot host Python project. Requires ``requirements.txt``  and  ````Procfile````.
- [Jquery Validate Plugin](https://jqueryvalidation.org/) - a jquery plugin used for form validation

## Testing

### Manual Testing

I used Google Developer tools to test different components

1. Website pages
    - Pages are responsive on different screen breakpoints.
    - There are no weirdly positioned elements.
    - Pages are mobile adaptable.

2. Form validation
    - Users are not allowed to submit a form without filling required input.
    - Throws an error message.
    - Placeholders appear in case of blank lines.

3. Modal 
    - Appears everytime to confirm an action was made either by submission or deletion of recipe.
    - Redirects to the updated page.

4. Submit button
    - Disabled until form is completed.

5. Product links
    - opens in a new tab

<!-- - HTML Validator Passed tests without issues
- CSS Validator Passed tests without issues
- JSHint Passed tests without issues
- PEP8 and AUTOPEP8 -->

## Deployment 

I use Gitpod IDE extension to clone Github repositories quickly. But you can do this too locally or on your chosen IDE.

1. Clone or download the Zip from Github

2. Make a new directory: 

    ````
    $ mkdir directory
    ````

    or  change directory to where you want to clone the repository:
   
    ````
    $ cd directory
    ````

3. Initialize Git

    ````
    $ git init
    ````

4. Paste the clone link

    ````
    $ git clone https://github.com/loulunds/3rd_Milestone_Project.git
    ````

5. Install Flask 

    ````
    $ pip3 install Flask
    ````

6. Make a requirements.txt file. Be sure you have installed all your chosen dependencies. In this project, I used an additional dependency Flask-PyMongo

    ````
    pip3 freeze --local > requirements.txt
    ````

7. Don't forget the Procfile. 

    ````
    $ echo web: python app.py > Procfile
    ````

In this project you need to set up environment variables so you can keep your sensitive information safe like passwords

1. Create an ``env.py`` and ``.gitignore`` file on root directory. Type env.py in your ``.gitignore`` file.

2. In ``env.py`` type:

    ````
    import os
    os.environ["variable name"] = "value of variable"
    ````
    In this project, I used Mongodb Atlas database so you need to make an account there then use "MONGO_URI" as variable and your MongoDB connection by going to ``Overview`` of your Cluster and click connect and choose option ``Connect your application`` and copy the link

3. Add this to your ``app.py`` file

    ````
    from os import path
    if path.exists("env.py") :
        import env

    ````
4. Now you can add this to app.py and your sensitive information is safe

    ````
    app.config["MONGO_URI"] = os.environ.get('MONGO_URI', 'mongodb://localhost')
    ````
This project is hosted in Heroku, to do that:

1. Create an app in Heroku

2. In your terminal, login to Heroku

    ````
    heroku login -i
    ````
3. Go to ``deploy`` and find the similar link. This will clone the app from your terminal. 

    ````
    $ heroku git:clone -a <app-name>
    ````

4. Before pushing, check if you have updated ``requirements.txt`` and ``Procfile`` then add variables to ``Config Variables`` option.
    
    ````
    <key>            <value>
    MONGO_URI     <your Mongo_URI link>
    IP            0.0.0.0
    PORT          5000
    SECRET_KEY    <SECRETKEY> if you have

5. if you have everything above, time to push to master

    ````
    $ git push origin master
    ````

## Credits


### Images 

- [Pixabay](https://pixabay.com/) - for free images

- [Imgur](https://imgur.com/) - for hosting my images

### Recipes
- [Google](https://www.google.com/) - for yummy chocolate recipes

### Codes
- [Stack Overflow](https://stackoverflow.com/)

- [Bootstrap](https://getbootstrap.com/)

- [MaterializeCSS](https://materializecss.com/)

- [Jinja](https://jinja.palletsprojects.com/)

## Acknowledgements

Thanks to my mentor, Dick Vlaanderen and to the tutor and student care support personnels of Code Institute.
Also, to the thousands of contributor in Slack and Slack Overflow.

## Disclaimer

This project is for educational purposes only. 

[Back to top](#)