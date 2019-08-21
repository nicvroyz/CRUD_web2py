# -*- coding: utf-8 -*-
if db(db.auth_user.id>0).isempty():
    # creando usuario admin por defecto
    password = db.auth_user.password.validate('testing')[0]
    id_admin = db.auth_user.insert(
                first_name='Admin',
                last_name='duoc',
                email='admin@duoc.cl',
                password=password
            )

    # creación de grupos por defecto
    id_sysadmin_group = db.auth_group.insert(role='Sysadmin',
        description='GOD PAN!')
    db.auth_group.insert(role='Administrador',
        description='Owner de una organizacion')
    db.auth_group.insert(role='Cliente',
        description='Pertenece a un cliente, solo puede ver')

    # creación de membresia por defecto para sysadmin
    db.auth_membership.insert(user_id=id_admin,group_id=id_sysadmin_group)
    pass

DB = db.define_table

DB(
    'profession',
    Field('name_profession'),
    format='%(name_profession)s'
)


DB(
    'gender',
    Field('option_gender'),
    format='%(option_gender)s'
)

DB(
    'years_exp',
    Field('experience'),
    format='%(experience)s'
)

DB(
    'employee',
    Field('rut', requires=IS_NOT_EMPTY(error_message="Este campo es obligatorio.")),
    Field('first_name', requires=IS_NOT_EMPTY(error_message="Este campo es obligatorio.")),
    Field('last_name', requires=IS_NOT_EMPTY(error_message="Este campo es obligatorio.")),
    Field('gender_id', 'reference gender'),
    Field('birth_date', 'date', requires=IS_NOT_EMPTY(error_message="Este campo es obligatorio.")),
    Field('email', requires=IS_NOT_EMPTY(error_message="Este campo es obligatorio.")),
    Field('phone', 'integer'),
    Field('address', requires=IS_NOT_EMPTY(error_message="Este campo es obligatorio.")),
    Field('profession_id', 'reference profession'),
    Field('exp_id', 'reference years_exp'),
    format='%(rut)s %(last_name)s %(first_name)s'
)