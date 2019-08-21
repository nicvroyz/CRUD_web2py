@auth.requires_membership('Sysadmin')
def new():
    form = SQLFORM(db.employee)
    if form.process().accepted:
        response.flash = 'empleado agregado'
    elif form.errors:
        print form.errors
    return dict(form = form)

@auth.requires_membership('Sysadmin')
def edit():
    employee_id = request.args(0) 
    form = SQLFORM(db.employee, employee_id)
    if form.process().accepted:
        response.flash = "Información de empleado actualizada correctamente"
        redirect(URL('default', 'index'))
    elif form.errors:
        response.flash = "Se ha producido un error en la actualización."
    return dict(form=form)

@auth.requires_membership('Sysadmin')
def delete():
    employee_id = request.args(0)
    deleted = db((db.employee.id == request.args(0))).delete() 
    if deleted:
        session.flash = 'El empleado ha sido eliminado exitosamente'
    redirect(URL('default', 'index'))
