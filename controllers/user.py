@auth.requires_membership('Sysadmin')
def index():
    dataset = db(db.auth_user).select()
    return dict(dataset=dataset)


@auth.requires_membership('Sysadmin')
def new():
    form = SQLFORM(db.auth_user)
    if form.process().accepted:
        response.flash='Usuario agregado'
        redirect(URL('user', 'index'))
    elif form.errors:
        response.flash = "Se encontraron errores en el ingreso"
        print form.errors
    return dict(form=form) 


@auth.requires_membership('Sysadmin')
def edit():
    auth_user_id = request.args(0) 
    form = SQLFORM(db.auth_user, auth_user_id)
    if form.process().accepted:
        response.flash = "Usuario actualizado correctamente"
        redirect(URL('user', 'index'))
    elif form.errors:
        response.flash = "Se ha producido un error en la actualización."
    return dict(form=form)


@auth.requires_membership('Sysadmin')
def delete():
    auth_user_id = request.args(0)
    deleted = db((db.auth_user.id == request.args(0))).delete() 
    if deleted:
        session.flash = 'El Usuario ha sido eliminado exitosamente'
    redirect(URL('user', 'index'))
