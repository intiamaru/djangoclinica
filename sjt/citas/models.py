from django.db import models

'''
Pacientes
 * Pacientes
Especialidades
Horarios
 1* Doctor
Medicos
 * Especialidades

Reservas (Citas)
 1* Horarios
 1* Paciente
'''

class Cita(models.Model):
    '''
    cod_paci char 8
    fec_cita datetime
    cod_medi char 6
    cod_turn char 1
    num_hora char 10
    nom_paci varchar
    cod_esta char 1
    cod_tipo char 1
    des_obse varchar
    cod_usuario char 8
    cod_tipo_docu char 3
    cod_seri_docu char 3
    num_docu char 8
    epago_fecha_hora datetime
    epago_total numeric
    '''
    #cod_paci = models.CharField(max_length=8)
    cod_paci = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    fec_cita = models.DateTimeField()
    #cod_medi = models.CharField(max_length=6)
    cod_medi = models.ForeignKey('Medico', on_delete=models.CASCADE)
    cod_turn = models.CharField(max_length=1)
    num_hora = models.CharField(max_length=10)
    nom_paci = models.TextField()
    cod_esta = models.CharField(max_length=1)
    cod_tipo = models.CharField(max_length=1)
    des_obse = models.TextField()
    cod_usuario = models.CharField(max_length=8)
    cod_tipo_docu = models.CharField(max_length=3)
    cod_seri_docu = models.CharField(max_length=3)
    num_docu = models.CharField(max_length=8)
    epago_fecha_hora = models.DateTimeField()
    epago_total = models.DecimalField(max_digits=6, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s , %s" % self.cod_paci, self.nom_paci

class Paciente(models.Model):
    '''
    cod_paci char 8
    ape_pate_paci varchar
    ape_mate_paci varchar
    nom_paci varchar
    fec_naci datetime
    cod_sexo char 1
    cod_estadocivi char 3
    cod_tipo_docu char 2
    des_dni char 15
    des_dire varchar
    '''
    cod_paci = models.CharField(max_length=8)
    ape_pate_paci = models.TextField()
    ape_mate_paci = models.TextField()
    nom_paci = models.TextField()
    fec_naci = models.DateTimeField()
    cod_sexo = models.CharField(max_length=1)
    cod_estadocivil = models.CharField(max_length=3)
    cod_tipo_docu = models.CharField(max_length=2)
    des_dni = models.CharField(max_length=15)
    des_dire = models.TextField()
    image = models.FilePathField(path="/img")

class Medico(models.Model):
    '''
    cod_medi char 6
    ape_pate_paci varchar
    ape_mate_paci varchar
    nom_paci varchar
    fec_naci datetime
    cod_sexo char 1
    cod_estadocivi char 3
    cod_tipo_docu char 2
    des_dni char 15
    des_dire varchar
    '''
    cod_paci = models.CharField(max_length=8)
    ape_pate_paci = models.TextField()
    ape_mate_paci = models.TextField()
    nom_medi = models.TextField()
    cod_cole_medi = models.CharField(max_length=18)
    cod_rne = models.CharField(max_length=6)
    num_tiem_cons = models.DecimalField(max_digits=6, decimal_places=2)
    num_tiem_cons = models.SmallIntegerField()
    num_cons_cita = models.SmallIntegerField()
    image = models.FilePathField(path="/img")

class Especialidad(models.Model):
    '''
    cod_espe char 3
    des_espe varchar
    cod_esta char 1
    '''
    cod_espe = models.CharField(max_length=3)
    des_espe = models.TextField()
    cod_esta = models.CharField(max_length=1)

class MedicoHorario(models.Model):
    '''
    cod_medi char 6
    num_dia char 1
    cod_turn char 1
    num_hora_ingr char 10
    num_hora_sali 10
    num_entr_cita numeric
    num_tiem_cons numeric
    num_cons_cita numeric
    cod_esta char 1

    '''
    #cod_medi = models.CharField(max_length=6)
    cod_medi = models.ForeignKey('Medico', on_delete=models.CASCADE)
    num_dia = models.CharField(max_length=1)
    cod_turn = models.CharField(max_length=1)
    num_hora_ingr = models.CharField(max_length=10)
    num_hora_sali = models.CharField(max_length=10)
    num_entr_cita = models.SmallIntegerField()
    num_tiem_cons = models.SmallIntegerField()
    num_cons_cita = models.SmallIntegerField()
