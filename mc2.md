# Mini challenge 2

## Functional posts app

durinng this mini challenge  the focus will be on creating a functional posts app.
This means that users should be able to create, read (detail view), update, delete and scan (list view) "posts".


### Accceptance Criteria
1. Create migrations
2. Run migrations
2.1. Optional: register the Post model onto the admin panel and create a few dummy posts.
3. Users should be able to create new posts.
4. Users should be able to read existing posts, one at a time (detail view).
5. Users should be able to update existing posts (you'll need a form)
5.1. The urlpattern for an update view *must have* a url parameter specifying the primary key of the post in question.
6. Users should be able to delete existing posts.
6.1. Note that for delete view, a form without fields is needed in the template (make sure you have CSRF token).
6.1.1. This form is a confirmation screen ensuring the user really wants to delete the specified record.
6.2. The delete view has access to the post in question, which can be rendered on the resulting template for visual confirmation.
6.2.1. The urlpattern for a delete view *must have* a url parameter specifying the primary key of the post in question.
7. Users should be able to see a list of posts (list view).
8. Test! Make sure all views are functional.
## Note
You will need a combination templates, urlpatterns *and* configurations to ensure these features work.