# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Drip.check_function'
        db.add_column(u'drip_drip', 'check_function',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


        # Changing field 'SentDrip.user'
        db.alter_column(u'drip_sentdrip', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.User']))

    def backwards(self, orm):
        # Deleting field 'Drip.check_function'
        db.delete_column(u'drip_drip', 'check_function')


        # Changing field 'SentDrip.user'
        db.alter_column(u'drip_sentdrip', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

    models = {
        u'accounts.company': {
            'Meta': {'ordering': "['name']", 'object_name': 'Company'},
            'account_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'credit_card': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.CreditCard']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_distributor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'payment_plan': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['billing.PaymentTier']", 'null': 'True', 'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'trialing'", 'max_length': '15'}),
            'stripe_customer_id': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255', 'blank': 'True'}),
            'stripe_testing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'trialing_days': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        },
        u'accounts.creditcard': {
            'Meta': {'object_name': 'CreditCard'},
            'card_type': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'exp_month': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'exp_year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last4': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'})
        },
        u'accounts.distributor': {
            'Meta': {'object_name': 'Distributor'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'clients': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Clients'", 'symmetrical': 'False', 'to': u"orm['accounts.Company']"}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.Company']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stripe_public_key': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255', 'blank': 'True'}),
            'stripe_secret_key': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '255', 'blank': 'True'})
        },
        u'accounts.user': {
            'Meta': {'ordering': "('username', 'first_name', 'last_name')", 'object_name': 'User'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.Company']", 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'billing.paymenttier': {
            'Meta': {'object_name': 'PaymentTier'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'distributor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.Distributor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_devices': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'min_devices': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'payment_interval': ('django.db.models.fields.CharField', [], {'default': "'year'", 'max_length': '15', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'stripe_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'trial_days': ('django.db.models.fields.IntegerField', [], {'default': '15'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'drip.drip': {
            'Meta': {'object_name': 'Drip'},
            'body_html_template': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'check_function': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'from_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'from_email_name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastchanged': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'message_class': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '120', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'subject_template': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'drip.querysetrule': {
            'Meta': {'object_name': 'QuerySetRule'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'drip': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'queryset_rules'", 'to': u"orm['drip.Drip']"}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'field_value': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastchanged': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'lookup_type': ('django.db.models.fields.CharField', [], {'default': "'exact'", 'max_length': '12'}),
            'method_type': ('django.db.models.fields.CharField', [], {'default': "'filter'", 'max_length': '12'})
        },
        u'drip.sentdrip': {
            'Meta': {'object_name': 'SentDrip'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'drip': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sent_drips'", 'to': u"orm['drip.Drip']"}),
            'from_email': ('django.db.models.fields.EmailField', [], {'default': 'None', 'max_length': '75', 'null': 'True'}),
            'from_email_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '150', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sent_drips'", 'to': u"orm['accounts.User']"})
        }
    }

    complete_apps = ['drip']