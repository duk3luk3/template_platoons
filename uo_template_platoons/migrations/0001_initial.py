# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Period'
        db.create_table('uo_template_platoons_period', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('start', self.gf('django.db.models.fields.DateField')()),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('uo_template_platoons', ['Period'])

        # Adding model 'Army'
        db.create_table('uo_template_platoons_army', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('side', self.gf('django.db.models.fields.CharField')(max_length=1, default='W')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('uo_template_platoons', ['Army'])

        # Adding model 'Branch'
        db.create_table('uo_template_platoons_branch', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('uo_template_platoons', ['Branch'])

        # Adding model 'Platoon'
        db.create_table('uo_template_platoons_platoon', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('army', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['uo_template_platoons.Army'])),
            ('branch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['uo_template_platoons.Branch'])),
            ('period', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['uo_template_platoons.Period'])),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('uo_template_platoons', ['Platoon'])

        # Adding model 'SectionDeployment'
        db.create_table('uo_template_platoons_sectiondeployment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['uo_template_platoons.Section'])),
            ('platoon', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['uo_template_platoons.Platoon'])),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('uo_template_platoons', ['SectionDeployment'])

        # Adding model 'Section'
        db.create_table('uo_template_platoons_section', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('uo_template_platoons', ['Section'])

        # Adding model 'UnitDeployment'
        db.create_table('uo_template_platoons_unitdeployment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['uo_template_platoons.Unit'])),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['uo_template_platoons.Section'])),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('uo_template_platoons', ['UnitDeployment'])

        # Adding model 'Unit'
        db.create_table('uo_template_platoons_unit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('uo_template_platoons', ['Unit'])


    def backwards(self, orm):
        # Deleting model 'Period'
        db.delete_table('uo_template_platoons_period')

        # Deleting model 'Army'
        db.delete_table('uo_template_platoons_army')

        # Deleting model 'Branch'
        db.delete_table('uo_template_platoons_branch')

        # Deleting model 'Platoon'
        db.delete_table('uo_template_platoons_platoon')

        # Deleting model 'SectionDeployment'
        db.delete_table('uo_template_platoons_sectiondeployment')

        # Deleting model 'Section'
        db.delete_table('uo_template_platoons_section')

        # Deleting model 'UnitDeployment'
        db.delete_table('uo_template_platoons_unitdeployment')

        # Deleting model 'Unit'
        db.delete_table('uo_template_platoons_unit')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Group']", 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False', 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'uo_template_platoons.army': {
            'Meta': {'object_name': 'Army'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'side': ('django.db.models.fields.CharField', [], {'max_length': '1', 'default': "'W'"})
        },
        'uo_template_platoons.branch': {
            'Meta': {'object_name': 'Branch'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'uo_template_platoons.period': {
            'Meta': {'object_name': 'Period'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'start': ('django.db.models.fields.DateField', [], {})
        },
        'uo_template_platoons.platoon': {
            'Meta': {'object_name': 'Platoon'},
            'army': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['uo_template_platoons.Army']"}),
            'branch': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['uo_template_platoons.Branch']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'period': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['uo_template_platoons.Period']"}),
            'sections': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['uo_template_platoons.Section']", 'symmetrical': 'False', 'through': "orm['uo_template_platoons.SectionDeployment']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'uo_template_platoons.section': {
            'Meta': {'object_name': 'Section'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'units': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['uo_template_platoons.Unit']", 'symmetrical': 'False', 'through': "orm['uo_template_platoons.UnitDeployment']"})
        },
        'uo_template_platoons.sectiondeployment': {
            'Meta': {'object_name': 'SectionDeployment'},
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'platoon': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['uo_template_platoons.Platoon']"}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['uo_template_platoons.Section']"})
        },
        'uo_template_platoons.unit': {
            'Meta': {'object_name': 'Unit'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'uo_template_platoons.unitdeployment': {
            'Meta': {'object_name': 'UnitDeployment'},
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['uo_template_platoons.Section']"}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['uo_template_platoons.Unit']"})
        }
    }

    complete_apps = ['uo_template_platoons']