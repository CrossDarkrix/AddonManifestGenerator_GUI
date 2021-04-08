import ui, json, uuid

def Resources_pack(manif):
	m = manif.superview
	pack_name = m['pack_name'].text
	pack_ver = m['Pack_Version'].text.replace('.',',').replace(' ',',')
	descript = m['descript'].text
	#Json Template
	raw_manifest = ("""{
	   "format_version" : 1,
	   "header" : {
		  "description" : "",
		  "name" : "",
		  "uuid" : "",
		  "version" : [PackVersion]
	   },
	   "modules" : [
		  {
			 "description" : "",
			 "type" : "",
			 "uuid" : "",
			 "version" : [PackVersion]
		  }
	   ]
	}
	""").replace('PackVersion', pack_ver)

	#JSON形式の読み込み
	load_manifest = json.loads(raw_manifest)

	#ここからUUID
	uuid_1 = str(uuid.uuid4()).replace('(','').replace(')','').replace('UUID','')
	uuid_2 = str(uuid.uuid4()).replace('(','').replace(')','').replace('UUID','')

	#ここからJSON内の値変更
	#"header"部分の値変更
	load_manifest['header']['description'] = descript
	load_manifest['header']['name'] = pack_name
	load_manifest['header']['uuid'] = uuid_1

	#"modules"部分の値変更
	load_manifest['modules'][0]['description'] = descript
	load_manifest['modules'][0]['type'] = 'resources'
	load_manifest['modules'][0]['uuid'] = uuid_2

	JSON_Data = json.dumps(load_manifest, indent=2, ensure_ascii=False)

	#manifest.jsonとして書き出し
	f = open('manifest.json','w', encoding='utf-8')
	f.write(JSON_Data)
	f.close()
	m['Create_Log'].text = JSON_Data

def Data_Resources_pack(manif):
	m = manif.superview
	pack_name = m['pack_name'].text
	pack_ver = m['Pack_Version'].text.replace('.',',').replace(' ',',')
	descript = m['descript'].text
	min_engines = m['min_engines'].text.replace('.',',').replace(' ',',')
	if min_engines == '':
		min_engines = ('1.11.0').replace('.',',').replace(' ',',')
	else:
		pass
	#Json Template
	raw_manifest = ("""{
	   "format_version" : 2,
	   "header" : {
		  "description" : "",
		  "name" : "",
		  "uuid" : "",
		  "min_engine_version": [MIN_VERSION],
		  "version" : [PackVersion]
	   },
	   "modules" : [
		  {
			 "description" : "",
			 "type" : "",
			 "uuid" : "",
			 "version" : [PackVersion]
		  }
	   ]
	}
	""").replace('PackVersion', pack_ver).replace('MIN_VERSION', min_engines)

	#JSON形式の読み込み
	load_manifest = json.loads(raw_manifest)

	#ここからUUID
	uuid_1 = str(uuid.uuid4()).replace('(','').replace(')','').replace('UUID','')
	uuid_2 = str(uuid.uuid4()).replace('(','').replace(')','').replace('UUID','')

	#ここからJSON内の値変更
	#"header"部分の値変更
	load_manifest['header']['description'] = descript
	load_manifest['header']['name'] = pack_name
	load_manifest['header']['uuid'] = uuid_1

	#"modules"部分の値変更
	load_manifest['modules'][0]['description'] = descript
	load_manifest['modules'][0]['type'] = 'resources'
	load_manifest['modules'][0]['uuid'] = uuid_2

	JSON_Data = json.dumps(load_manifest, indent=2, ensure_ascii=False)

	#manifest.jsonとして書き出し
	f = open('manifest.json','w', encoding='utf-8')
	f.write(JSON_Data)
	f.close()
	m['Create_Log'].text = JSON_Data
	

def behava_pack(manif):
	m = manif.superview
	pack_name = m['pack_name'].text
	pack_ver = m['Pack_Version'].text.replace('.',',').replace(' ',',')
	descript = m['descript'].text
	min_engines = m['min_engines'].text.replace('.',',').replace(' ',',')
	if min_engines == '':
		min_engines = ('1.11.0').replace('.',',').replace(' ',',')
	else:
		pass

	raw_data_manifest = ("""{
	   "format_version" : 2,
	   "header" : {
		  "description" : "",
		  "name" : "",
		  "uuid" : "",
		  "min_engine_version": [MIN_VERSION],
		  "version" : [PackVersion]
	   },
	   "modules" : [
		  {
			 "description" : "",
			 "type" : "",
			 "uuid" : "",
			 "version" : [PackVersion]
		  }
	   ]
	}
	""").replace('PackVersion', pack_ver).replace('MIN_VERSION', min_engines)

	#JSON形式の読み込み
	load_manifest = json.loads(raw_data_manifest)

	#ここからUUID
	uuid_1 = str(uuid.uuid4()).replace('(','').replace(')','').replace('UUID','')
	uuid_2 = str(uuid.uuid4()).replace('(','').replace(')','').replace('UUID','')

	#ここからJSON内の値変更
	#"header"部分の値変更
	load_manifest['header']['description'] = descript
	load_manifest['header']['name'] = pack_name
	load_manifest['header']['uuid'] = uuid_1

	#"modules"部分の値変更
	load_manifest['modules'][0]['description'] = descript
	load_manifest['modules'][0]['type'] = 'data'
	load_manifest['modules'][0]['uuid'] = uuid_2

	JSON_Data = json.dumps(load_manifest, indent=2, ensure_ascii=False)

	#manifest.jsonとして書き出し
	f = open('manifest.json','w', encoding='utf-8')
	f.write(JSON_Data)
	f.close()
	m['Create_Log'].text = JSON_Data

def skins_pack(manif):
	m = manif.superview
	pack_name = m['pack_name'].text
	pack_ver = m['Pack_Version'].text.replace('.',',').replace(' ',',')
	descript = m['descript'].text
	#Json Template
	raw_manifest = ("""{
	   "format_version" : 1,
	   "header" : {
		  "description" : "",
		  "name" : "",
		  "uuid" : "",
		  "version" : [PackVersion]
	   },
	   "modules" : [
		  {
			 "description" : "",
			 "type" : "",
			 "uuid" : "",
			 "version" : [PackVersion]
		  }
	   ]
	}
	""").replace('PackVersion', pack_ver)

	#JSON形式の読み込み
	load_manifest = json.loads(raw_manifest)

	#ここからUUID
	uuid_1 = str(uuid.uuid4()).replace('(','').replace(')','').replace('UUID','')
	uuid_2 = str(uuid.uuid4()).replace('(','').replace(')','').replace('UUID','')

	#ここからJSON内の値変更
	#"header"部分の値変更
	load_manifest['header']['description'] = descript
	load_manifest['header']['name'] = pack_name
	load_manifest['header']['uuid'] = uuid_1

	#"modules"部分の値変更
	load_manifest['modules'][0]['description'] = descript
	load_manifest['modules'][0]['type'] = 'skinpack'
	load_manifest['modules'][0]['uuid'] = uuid_2

	JSON_Data = json.dumps(load_manifest, indent=2, ensure_ascii=False)

	#manifest.jsonとして書き出し
	f = open('manifest.json','w', encoding='utf-8')
	f.write(JSON_Data)
	f.close()
	m['Create_Log'].text = JSON_Data

def main(manif):
	m = manif.superview
	resource_p_sw = m['Resource_sw'].value
	data_resource_p_sw = m['Data_Resource_sw'].value
	behava_p_sw = m['BehavaPack_sw'].value
	skin_p_sw = m['SkinPack_sw'].value
	
	if resource_p_sw:
		Resources_pack(manif)
	if data_resource_p_sw:
		Data_Resources_pack(manif)
	if behava_p_sw:
		behava_pack(manif)
	if skin_p_sw:
		skins_pack(manif)

v = ui.load_view()
v.present('sheet')
