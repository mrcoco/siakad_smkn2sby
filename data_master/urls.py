from django.conf.urls import patterns, url, include
from data_master import views

urlpatterns = patterns('data_master',
    #url(r'^$', views.data_master, name='data_master'),
    url(r'^jabatan/$', views.jabatan, name='jabatan'),
    url(r'^jabatan/tambah/$', views.tambah_jabatan, name='tambah_jabatan'),
    url(r'^jabatan/ubah/(?P<idData>\d+)/$', views.ubah_jabatan, name='ubah_jabatan'),
    url(r'^jabatan/hapus/(?P<idData>\d+)/$', views.hapus_jabatan, name='hapus_jabatan'),
    url(r'^pangkat/$', views.pangkat, name='pangkat'),
    url(r'^pangkat/tambah/$', views.tambah_pangkat, name='tambah_pangkat'),
    url(r'^pangkat/ubah/(?P<idData>\d+)/$', views.ubah_pangkat, name='ubah_pangkat'),
    url(r'^pangkat/hapus/(?P<idData>\d+)/$', views.hapus_pangkat, name='hapus_pangkat'),
    url(r'^jurusan/$', views.jurusan, name='jurusan'),
    url(r'^jurusan/tambah/$', views.tambah_jurusan, name='tambah_jurusan'),
    url(r'^jurusan/ubah/(?P<idData>\d+)/$', views.ubah_jurusan, name='ubah_jurusan'),
    url(r'^jurusan/hapus/(?P<idData>\d+)/$', views.hapus_jurusan, name='hapus_jurusan'),
    url(r'^tahun_ajaran/$', views.thnajaran, name='thnajaran'),
    url(r'^tahun_ajaran/tambah/$', views.tambah_thnajaran, name='tambah_thnajaran'),
    url(r'^tahun_ajaran/ubah/(?P<idData>\d+)/$', views.ubah_thnajaran, name='ubah_thnajaran'),
    url(r'^tahun_ajaran/hapus/(?P<idData>\d+)/$', views.hapus_thnajaran, name='hapus_thnajaran'),
    url(r'^ruang/$', views.ruang, name='ruang'),
    url(r'^ruang/tambah/$', views.tambah_ruang, name='tambah_ruang'),
    url(r'^ruang/ubah/(?P<idData>\d+)/$', views.ubah_ruang, name='ubah_ruang'),
    url(r'^ruang/hapus/(?P<idData>\d+)/$', views.hapus_ruang, name='hapus_ruang'),
    url(r'^mapel/', include('mapel.urls')),
    url(r'^kompetensi/', include('mapel.kompetensi_urls')),
    url(r'^mapelun/', include('mapel.urls_un')),
    )