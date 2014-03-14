# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Period.id'
        db.delete_column('uo_template_platoons_period', 'id')


        # Changing field 'Period.name'
        db.alter_column('uo_template_platoons_period', 'name', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=1024))
        # Adding unique constraint on 'Period', fields ['name']
        db.create_unique('uo_template_platoons_period', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Period', fields ['name']
        db.delete_unique('uo_template_platoons_period', ['name'])


        # User chose to not deal with backwards NULL issues for 'Period.id'
        raise RuntimeError("Cannot reverse this migration. 'Period.id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Period.id'
        db.add_column('uo_template_platoons_period', 'id',
                      self.gf('django.db.models.fields.AutoField')(primary_key=True),
                      keep_default=False)


        # Changing field 'Period.name'
        db.alter_column('uo_template_platoons_period', 'name', self.gf('django.db.models.fields.CharField')(max_length=1024))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType'},
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
            'name': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '1024'}),
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
            'sections': ('django.db.models.fields.related.ManyToManyField', [], {'through': "orm['uo_template_platoons.SectionDeployment']", 'symmetrical': 'False', 'to': "orm['uo_template_platoons.Section']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'uo_template_platoons.section': {
            'Meta': {'object_name': 'Section'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'units': ('django.db.models.fields.related.ManyToManyField', [], {'through': "orm['uo_template_platoons.UnitDeployment']", 'symmetrical': 'False', 'to': "orm['uo_template_platoons.Unit']"})
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