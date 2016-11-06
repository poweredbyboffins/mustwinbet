# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.


from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class Betdata(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    competition = models.TextField(blank=True)
    marketid = models.TextField(db_column='marketId', blank=True)  # Field name made lowercase.
    totalmatched = models.FloatField(db_column='totalMatched', blank=True, null=True)  # Field name made lowercase.
    marketname = models.TextField(db_column='marketName', blank=True)  # Field name made lowercase.
    event = models.TextField(blank=True)
    runners = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'betdata'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Factordata(models.Model):
    id = models.BigIntegerField(primary_key=True)
    hometeam = models.CharField(max_length=80, blank=True)
    awayteam = models.CharField(max_length=80, blank=True)
    matchdate = models.DateField(blank=True, null=True)
    fthg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ftag = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ftr = models.CharField(max_length=2, blank=True)
    winprob = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    drawprob = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    loseprob = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pctwin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pctnotwin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    homeformadj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    awayformadj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factordata'


"""
class Factordata2(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    hometeam = models.CharField(max_length=80, blank=True)
    awayteam = models.CharField(max_length=80, blank=True)
    matchdate = models.DateField(blank=True, null=True)
    fthg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ftag = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ftr = models.CharField(max_length=2, blank=True)
    winprob = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    drawprob = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    loseprob = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pctwin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pctnotwin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    homeformadj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    awayformadj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factordata2'

"""

class Frontpage(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=200, blank=True)
    blurb = models.CharField(max_length=2000, blank=True)
    image = models.CharField(max_length=250, blank=True)

    class Meta:
        managed = False
        db_table = 'frontpage'


class Gamepred(models.Model):
    id = models.BigIntegerField(primary_key=True)
    hometeam = models.CharField(max_length=80, blank=True)
    awayteam = models.CharField(max_length=80, blank=True)
    matchdate = models.DateField(blank=True, null=True)
    fthg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ftag = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ftr = models.CharField(max_length=2, blank=True)
    winprob = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    drawprob = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    loseprob = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pctwin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    pctnotwin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    homeformadj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    awayformadj = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    active_ind = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'gamepred'


class Games(models.Model):
    hometeam = models.CharField(max_length=80, blank=True)
    awayteam = models.CharField(max_length=80, blank=True)
    winprob = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    loseprob = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    drawprob = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    gamedate = models.DateField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)  # AutoField?
    compid = models.CharField(max_length=10, blank=True)
    comname = models.CharField(max_length=50, blank=True)
    active = models.CharField(max_length=1, blank=True)

    class Meta:
        managed = False
        db_table = 'games'


class Register(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    type = models.CharField(max_length=100, blank=True)
    blurb = models.CharField(max_length=2000, blank=True)

    class Meta:
        managed = False
        db_table = 'register'


class Rescut(models.Model):
    div = models.CharField(max_length=10, blank=True)
    matchdate = models.DateField(blank=True, null=True)
    hometeam = models.CharField(max_length=80, blank=True)
    awayteam = models.CharField(max_length=80, blank=True)
    fthg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ftag = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ftr = models.CharField(max_length=2, blank=True)
    hthg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    htag = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    htr = models.CharField(max_length=2, blank=True)
    id = models.IntegerField(primary_key=True)  # AutoField?

    class Meta:
        managed = False
        db_table = 'rescut'


class Results(models.Model):
    div = models.CharField(max_length=10, blank=True)
    matchdate = models.DateField(blank=True, null=True)
    hometeam = models.CharField(max_length=80, blank=True)
    awayteam = models.CharField(max_length=80, blank=True)
    fthg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ftag = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ftr = models.CharField(max_length=2, blank=True)
    hthg = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    htag = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    htr = models.CharField(max_length=2, blank=True)
    referee = models.CharField(max_length=80, blank=True)
    hs = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    aws = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hst = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ast = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hhw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ahw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ac = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hf = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    af = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ho = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ao = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hy = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ay = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hr = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ar = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hbp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    abp = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    gbh = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    gbd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    gba = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    iwh = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    iwd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    iwa = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lbh = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lbd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lba = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sbh = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sbd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sba = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    whh = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    whd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    wha = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sjh = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sjd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sja = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vch = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vcd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    vca = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bb1x2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bbmxh = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bbavh = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bbmxd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bbavd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bbmxa = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bbava = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bbou = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bbmxgt25 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bbavgt25 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bbmxlt25 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bbavlt25 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bbah = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bbahh = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bbmxahh = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bbavahh = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bbmxaha = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bbavaha = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'results'



class Wldlypct(models.Model):
    win = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    draw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lose = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hometeam = models.CharField(max_length=80, blank=True)

    class Meta:
        managed = False
        db_table = 'wldlypct'


class Wldlypct2(models.Model):
    win = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    draw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lose = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hometeam = models.CharField(max_length=80, blank=True)

    class Meta:
        managed = False
        db_table = 'wldlypct2'


class Wldpct(models.Model):
    win = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    draw = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    lose = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hometeam = models.CharField(max_length=80, blank=True)

    class Meta:
        managed = False
        db_table = 'wldpct'
