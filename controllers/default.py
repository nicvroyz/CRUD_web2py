@auth.requires_login()
def index():
    dataset = db(db.employee).select()

    from datetime import datetime, timedelta
    form = SQLFORM.factory(
        Field('rut',requires=IS_NOT_EMPTY()),
        submit_button='Buscar'
    )
    return dict(dataset=dataset)


    def validate_rut(form):
        # calculando digito verificador para corroborar contra el sitema
        rut = form.vars.rut
        try:
            a = int(rut)
        except:
            form.errors.rut = 'Formato incorrecto'
        if len(rut)<7:
            form.errors.rut = 'Formato incorrecto'
    if form.process(onvalidation=validate_rut).accepted:
        rut = form.vars.rut.zfill(8)
        total =  int(rut[0])*3
        total += int(rut[1])*2
        total += int(rut[2])*7
        total += int(rut[3])*6
        total += int(rut[4])*5
        total += int(rut[5])*4
        total += int(rut[6])*3
        total += int(rut[7])*2
        dv = 11-(total%11)
        if dv == 11:
            dv = 0
        elif dv == 10:
            dv = 'k'
        rut = "{}-{}".format(rut,dv)
        if rut[0]=='0':
            rut = rut[1:]
        print rut
    elif form.errors:
        response.flash = 'Ingrese un rut para buscar'

    return dict(form=form)


# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)