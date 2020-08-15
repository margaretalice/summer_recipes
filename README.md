<h1>Peaches in the Summer: An online Cookbook.</h1>
<p>'Peaches in the Summer' is an online cookbook app, built with Flask, and MONGODB,whose aim is to allow the user to store traditional, or contemporary British recipes in one place. These might be recipes handed down, and treasured in families, or discovered on holidays in the UK, or found through research in books, and magazines,and TV shows.</p>
<p>The user will be able to create, read, update, and delete recipes as they choose, and even to edit, or add new categories e.g. spring could be divided into two categories such as 'early' spring recipes, or 'late' spring recipes, or a new category such as 'Feast Days and Festivals' could be added. This allows the user a great deal of creativity, and the ability, and flexibility to make the cookbook their own.</p>
<p>The app is scalable, and fully responsive, and easy to navigate. It uses Python3 for its backend logic, and the Flask framework. Bootatrap themes(clean blog) was uses to give a modern, fresh feel to the app. Where necessary for functioning, jQuery was used with Bootstrap, and Materialize was additionally used particularly with the'accordians' dropdown choices of categories, recipe,names, recipe description, recipe methods.<p>
<h2>UX</h2>
<p>I created the wireframes and mockups for small screens first, and then adapted them to medium , and larger screens, They can be viewed here:</p>
<p>My intentions for this app were:</p>
<ul>
<li>To creat an online cookbook for those interested in British cookery, whether historical, family based, or contemporary.
</li>
<li>It would be split into four categories for each season, spring, summer, autumn, and winter, though these could be added to, or edited.</li>
<li>I wanted pages for each season reflecting what sort of dishes would be appropriate for that particular time of year. Four cards would display a picture, and enticing description of a recipe, which the user could then click on a button to find fuller details of preparation, ingredients needed, and the method of cooking.</li>
<li>The app would be visually appealing with a cool, contemporary appearance, which I felt was appropriate for an online cookbook.</li
>
<li>The user would be able to create, read, update recipes to their tastes, and delete those they felt were not of interest to them.</li>
<p>The navigation bar is responsive having break points for smaller, medium, and larger screens. At screens smaller than 360px, the navbar toggles into a dropdown menu suitable for mobils devices.</p>
<p>The user is greeted on the homepage with a fresh, appealing picture of peaches aimed at enticing the viewer to explore the app further. There is a brief description of the app, and its purpose, followed by an encouragement to the reader to add their own selection of recipes.</p>
<p> The season pages have an appropriate picture to set the tone of the sort of recipes which might be appropriate and which the user might feel like cooking in this particular season.</p>
<p> The 'Add Recipes' and 'Edit Recipes' pages contain a form, helpfully broken up into sections for the user to input in a systematic, and consistent manner their new information.</p>
<h2>Technologies Used.</h2>
<ul>
<li>HTML5</li>
<li>CSS</li>
<li>Python3</li>
<li>Flask 1.0.2</li>
<li>Bootstrap 4.3.1</li>
<li>Javascript</li>
<li>jQuery</li>
<li>MONGODB, a document-oriented database used for the application database.</li>
<li>Atlas</li>
<li>Materialize</li>
<li>Markdown used to write README.md</li>
<li>Pycharm CE IDE was used as the IDE to write the web application.</li>
<li>Google Fonts</li>
<li>Git for version control</li>
<li>Github as the remote repository</li>
<li>Heroku</li>
</ul>
<p>All my HTML nd CSS was checked using the following validators:
<ul>
<li>HTML Validator</li>
<li>CSS Validator</li>
</ul>
<h2>Testing</h2>
<p>I set flask's debugger to true, so that when any error occured I could get guidance on the nature of the error because flask would display this error in the view explaining why the app had crashed.</p>
<p> Myost of the testing I did was manual, and every step was contiually tested to make sure that the app ran successfully. When I encountered the errors, I worked tirelessly to try and resolve them. I checked that when the user clicked on one of the season pages, the recipe cards would display along with the appropriate image, description and link to the full recipe on 'recipes.html' page9'recipes' on the navbar.</p>
<p>Clicking on 'recipes' gave a detailed view of all the recipes from each season category.</p>
<p>I checked that when clicking on 'categories' each category created in MONGODB would appear along with an edit and delete button, and that the edit button took you to an edit category form where you could edit the category and save the changes, and I further checked that these changes were made in my MONGODB database. I checked, and then restore that if a category was deleted it, too, was deleted from the MONGODB database.</p>
<h2>Database Schema</h2>
<p>The database scheme that I used was:
<ul>
<li>
user_name
</li>
<li>user_description</li>
<li>user_category</li>
<li>user_ingredients</li>
<li>user_method</li>
</ul>
</p>





