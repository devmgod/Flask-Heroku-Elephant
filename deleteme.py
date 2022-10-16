#query this comic
    comic = Comic.query.get_or_404(id) 

    form = EditComicsForm()

    #check authorization
    if comic.owner_id == current_user:

        #form validation
        
        if form.validate_on_submit(): #csrf & is POST

            comic.owner = form.owner.data
            comic.comictitle = form.comictitle.data
            comic.issuenumber = form.issuenumber.data
            comic.year = form.year.data
            comic.price = form.price.data
            comic.publisher = form.publisher.data
            comic.pedigree = form.pedigree.data
            comic.source = form.source.data
            comic.grade = form.grade.data
            comic.notes = form.notes.data



            db.session.add(comic)
            db.session.commit()

            flash(f"Successfully added {comictitle}")
        return redirect("/mystuff") 

    else:
         return render_template("edit-comic.html", 
         comic=comic, form=form)



    #if authorization fails...
    return render_template("search.html")