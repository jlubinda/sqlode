import psycopg2

class sqlQueries:
	def __init__(self):
		''' Constructor for this class. '''
		# Create some member animals
	
	def tablesList(self,tables,tableName,fields,feature_type,feature_access):
		#Feature Outputs (DO NOT EDIT)
		tables[tableName] = {"name":tableName,"type":feature_type,"access":feature_access,"fields":fields})
		return tables
	
	def createTable(self,dbType,table,sqlJSON):
		myFeature = sqlJSON[table]
		if(is_array(myFeature)) :
			if dbType.upper()=="POSTGRESQL":
				sql = "CREATE TABLE IF NOT EXISTS `"+table+"` (`ID` BIGSERIAL PRIMARY KEY,`APIKey` VARCHAR(255) NOT NULL "
			elif( dbType.upper()=="MYSQL"):
				sql = "CREATE TABLE IF NOT EXISTS `"+table+"` (`ID` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,`APIKey` VARCHAR(255) NOT NULL "
			elif( dbType.upper()=="SQLITE"):
				sql = "CREATE TABLE IF NOT EXISTS `"+table+"` (`ID` SERIAL PRIMARY KEY,`APIKey` VARCHAR(255) NOT NULL "
			#print_r(table);
			foreign_key = myFeature["foreign_key"]
			references = myFeature["references"]
			fields = myFeature["fields"]
			numFields = len(fields); #the record id
			#echo table.' '.$numFields."<br>";
			uniqueList = ""
			
			for a in range(numFields):
				fieldKey = fields[a]['Key']
				fieldNull = fields[a]['Null']
				fieldType = fields[a]['Type']
				
				sql = sql+",`"+fields[a]['Field']+"` "
				
				if(fieldKey.upper()=="UNI" or fieldKey.upper()=="UNIQUE" or fieldKey.upper()=="PRI" or fieldKey.upper()=="PRIMARY"):
					if(uniqueList==""):
						uniqueList = uniqueList + fields[a]['Field']
					else:
						uniqueList = uniqueList+ ","+fields[a]['Field
				
				if(fieldType.lower()=="int" or fieldType.lower()=="varchar" or fieldType.lower()=="varbinary" or fieldType.lower()=="binary" or fieldType.lower()=="char" or fieldType.lower()=="bit" or fieldType.lower()=="tinyint" or fieldType.lower()=="bigint" or fieldType.lower()=="smallint" or fieldType.lower()=="mediumint"):
					sql = sql+ fieldType+"("+fields[a]['length']+")":
				else:
					sql = sql+ fieldType
				
				if(fieldNull.upper()=='NO' or fieldNull.upper()=='NOT NULL'):
					sql = sql+ " NOT NULL"
				else:
					sql = sql+ " NULL"
				
				if(fields[a]['default']!=null and fieldNull!=''):
					sql = sql+ " DEFAULT "+fields[a]['default']
				
			sql = sql+ ", `transaction_by` VARCHAR(255) NOT NULL,`dateset` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP"
			if(uniqueList!=""):
				sql = sql+ ",CONSTRAINT "+table+"_unique UNIQUE ("+uniqueList+")"
			
			sql = sql+ ") "
			
			if(foreign_key!="" and references!=""):
				sql = sql+ "FOREIGN KEY ("+foreign_key+") "
				sql = sql+ "REFERENCES "+references+" ("+foreign_key+") "
			
			if dbType.upper()=="POSTGRESQL":
				sql = sql+ ";"
			elif(dbType.upper()=="MYSQL"):
				sql = sql+ " ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;"
			elif(dbType.upper()=="SQLITE"):
				sql = sql+ ";"
				
			
			
			#Insert some values
			res = mysqli_query($db,sql)
			
			if(res):
				output = 1
			else:
				output = 2
		else:
			output = 0
		
		return output
		
	def setupModule(self,dbType,location=""):
		import json

		# Opening JSON file 
		f = open(location+'tables.json',) 
		 
		# returns JSON object as a dictionary 
		data = json.load(f) 
		  
		output = []
		
		# Iterating through the json list 
		for for key in data: 
			tableName = key
			fields = []
			output[tableName] = self.createTable(dbType,tableName,data)
		
		# Closing file 
		f.close()
		
		return output
	
	def queryBuilder(self,qry,logic,d,a,e="",end="",postEnd=""):
		output = ""
		if(a!=""):
			if(a[0]=="!"):
				x = a[1:]
				if(x[0]=="~"):
					y =  x[1:]
					if(y[0]=="%"):
						b = y[1:]
						c = "NOT LIKE '"+b+"%'"
					else:
						b = substr_replace(x, "", 0,(1-num2))
						c = "NOT LIKE '"+b+"'"
					
					if(qry==""):
						output = " `"+d+"` "+c+""+end
					else:
						output = qry+" "+logic+" `"+d+"` "+c+""+end
				elif(x[0]=="%"):
					y =  substr_replace(x, "", 0,(1-num2))
					if(y[0]=="%"):
						b = y[1:]
						c = "NOT LIKE '%"+b+"%'"
					else:
						b = y
						c = "NOT LIKE '%"+b+"'"
					
					if(qry==""):
						output = " `"+d+"` "+c+""+end
					else:
						output = qry+" "+logic+" `"+d+"` "+c+""+end
				elif(x[0]=="="):
					b = x[1:]
					c = "!= '"+b+"'"
					
					if(qry==""):
						output = " `"+d+"` "+c+""+end
					else:
						output = qry+" "+logic+" `"+d+"` "+c+""+end
				elif(x[0]=="|"):
					b = x[1:]
					c = "NOT BETWEEN '"+b+"'"
					
					if(qry==""):
						output = " `"+d+"` NOT BETWEEN '"+b+"' AND '"+e+"' "+end
					else:
						output = " "+logic+" `"+d+"` NOT BETWEEN '"+b+"' AND '"+e+"' "+end
				elif(x[0]==">"):
					y = x[1:]
					
					if(y[0]=="="):
						b = y[1:]
						c = "<= '"+b+"'"
					else:
						c = "< '"+y+"'"
					
					if(qry==""):
						output = " `"+d+"` "+c+""+end
					else:
						output = qry+" "+logic+" `"+d+"` "+c+""+end
				elif(x[0]=="<"):
					y = x[1:]
					
					if(y[0]=="="):
						b = y[1:]
						c = ">= '"+b+"'"
					else:
						c = "> '"+y+"'"
					
					if(qry==""):
						output = " `"+d+"` "+c+""+end
					else:
						output = qry+" "+logic+" `"+d+"` "+c+""+end
				elif(x[0]=="^"):
					b = x[1:]
					c = "NOT IN '"+b+"'"
					
					if(qry==""):
						output = " `"+d+"` "+c+""+end
					else:
						output = qry+" "+logic+" `"+d+"` "+c+""+end
			else:
				x = a[1:]
				if(x[0]=="~"):
					y =  x[1:]
					if(y[0]=="%"):
						b = y[1:]
						c = "LIKE '"+b+"%'"
					else:
						b = x[1:]
						c = "LIKE '"+b+"'"
					
					if(qry==""):
						output = " `"+d+"` "+c+""+end
					else:
						output = qry+" "+logic+" `"+d+"` "+c+""+end
				elif(x[0]=="%"):
					y =  x[1:]
					if(y[0]=="%"):
						b = y[1:]
						c = "LIKE '%"+b+"%'"
					else:
						b = y
						c = "LIKE '%"+b+"'"
					
					if(qry==""):
						output = " `"+d+"` "+c+""+end
					else:
						output = qry+" "+logic+" `"+d+"` "+c+""+
				elif(x[0]=="="):
					b = x[1:]
					c = "= '"+b+"'"
					
					if(qry==""):
						output = " `"+d+"` "+c+""+end
					else:
						output = qry+" "+logic+" `"+d+"` "+c+""+end
				elif(x[0]=="|"):
					b = x[1:]
					
					if(qry==""):
						output = " `"+d+"` BETWEEN '"+b+"' AND '"+e+"' "+end
					else:
						output = " "+logic+" `"+d+"` BETWEEN '"+b+"' AND '"+e+"' "+end
				elif(x[0]==">"):
					y = x[1:]
					
					if(y[0]=="="):
						b = y[1:]
						c = ">= '"+b+"'"
					else:
						c = "> '"+y+"'"
					
					if(qry==""):
						output = " `"+d+"` "+c+""+end
					else:
						output = qry+" "+logic+" `"+d+"` "+c+""+end
				elif(x[0]=="<"):
					y = x[1:]
					num3 = len(y)
					
					if(y[0]=="="):
						b = y[1:]
						c = "<= '"+b+"'"
					else:
						c = "< '"+y+"'"
					
					if(qry==""):
						output = " `"+d+"` "+c+""+end:
					else:
						output = qry+" "+logic+" `"+d+"` "+c+""+end
				elif(x[0]=="^"):
					b = x[1:]
					c = "IN '"+b+"'"
					
					if(qry==""):
						output = " `"+d+"` "+c+""+end:
					else:
						output = qry+" "+logic+" `"+d+"` "+c+""+end
				else:
					c = "= '"+a+"'"
					
					if(qry==""):
						output = " `"+d+"` "+c+""+end
					else:
						output = qry+" "+logic+" `"+d+"` "+c+""+end
		else:
			output = qry
			
		return output+postEnd


	def paginator(myCurrentPage,limit_w,totalNumOfRecords_w,OrderBy,myCurrentDataOrder="ID",groupby=""):
		
		if type(limit_w) == int:
			limit = limit_w
		else:
			limit = int(limit_w)
		
		if type(totalNumOfRecords_w) == int:
			totalNumOfRecords = totalNumOfRecords_w
		else:
			totalNumOfRecords = int(totalNumOfRecords_w)
		
		if(myCurrentPage=="" or myCurrentPage==None):
			page = 1
		else:
			if type(myVariable) == int or type(myVariable) == float:
				if type(myVariable) == int:
					page = myCurrentPage
				else:
					page = int(myCurrentPage)
			else:
				page = 1
		
		upper_limit = (page*limit)
		lower_limit = (page*limit)-limit
		
		pagesx = totalNumOfRecords/limit
		pagesy = int(pagesx)
		if(pagesx>pagesy):
			pagesz = pagesy+1
			pagesv = int(pagesz)
		else:
			pagesv = int(pagesy)
		
		pages = pagesv

		if(myCurrentDataOrder=="DESC"):
			Order = "ASC"
		else:
			Order = "DESC"

		pageArray = []
		
		f = 0
		for f in range(pages):
			b = f + 1
			
			if(b==1 or b==0)
			{
				prevpage = 0
			}
			else
			{
				prevpage = b-1
			}
			
			if(pages==b)
			{
				nextpage = b
			}
			else
			{
				nextpage = b+1
			}
			
			if(b==page):
				pageArray.append({"prevpage":prevpage,"page":b,"nextpage":nextpage,"order":myCurrentDataOrder,"neworder":Order,"current":1})
			else:
				pageArray.append({"prevpage":prevpage,"page":b,"nextpage":nextpage,"order":myCurrentDataOrder,"neworder":Order,"current":0})
			
			
		queryLimiterAndSOrter = groupby+" order by "+OrderBy." "+myCurrentDataOrder+" LIMIT "+str(lower_limit)+", "+str(limit)
		
		result = {"pages":pages,"pageArray":pageArray,"order":myCurrentDataOrder,"neworder":Order,"upper_limit":upper_limit,"lower_limit":lower_limit,"queryLimiterAndSorter":queryLimiterAndSOrter}
		
		return result
		
 
	def edit_query_builder(self,qry,a,b):
		if(b=="" or b==None):
			output = ""
		else:
			if(qry=="" or qry==None):
				output = " `"+a+"` = '"+b+"' "
			else:
				output = qry+", `"+a+"` = '"+b+"' "
		return output
	
	
	
	def selectOne(self,APIKey,appName,environx,dbTable,sqlJSON):
		sqlDict = ast.literal_eval(sqlJSON)
		limiterDict = sqlDict["limiter"]
		whereJSON = sqlDict["where"]
		order_by = limiterDict["order_by"]
		order = limiterDict["order"]
		limit_min = limiterDict["limit_min"]
		limit_max = limiterDict["limit_max"]
		
		if not environx or environx=="":
			environ = ""
		else:
			environ = environx
		
		import json
		
		with open(appName+'_config.json') as json_file1:
			connDict = json.load(json_file1)
		
		with open(dbTable+'.json') as json_file2:
			tableConfigs = json.load(json_file2)
		
		if not whereJSON or whereJSON=="":
			whereDict = {}
		else:
			whereDict = whereJSON
		
		qry2 = " WHERE APIKey = '"+str(APIKey)+"' "
		qry = ""
		
		for a in range(len(whereDict)):
			dict = whereDict[a]
			
			if dict["value2"]=="" or not dict["value2"]:
				qry = self.queryBuilder(qry,dict["next_field_logic"],dict["column"],dict["value"],"","")
			else:
				qry = queryBuilder(db,qry,dict["next_field_logic"],dict["column"],dict["value"],dict["value2"],dict["pre_bracket"],dict["post_bracket"])
		
		if qry==")" or qry=="" or not qry:
			qry2 = qry2
			qry = ""
		else:
			qry2 = qry2+" AND ("
		
		eoq = "SELECT MAX(ID) FROM "+dbTable+""+qry2+qry+" "
		
		sql = "SELECT ID,"
		for p in tableConfigs['columns']:
			sql = sql+p["name"]+","
		
		sql = sql+"transaction_by,dateset FROM WHERE ID = ("+eoq+")"
		
		conn = psycopg2.connect(host=connDict["host"],database=connDict["database"+environ],user=connDict["user"],password=connDict["password"])
		cur = conn.cursor()
		cur.execute(sql)
		output = cur.fetchone()
		cur.close()
		return output
 
	def selectMany(self,APIKey,appName,environx,dbTable,sqlJSON):
		sqlDict = ast.literal_eval(sqlJSON)
		limiterDict = sqlDict["limiter"]
		whereJSON = sqlDict["where"]
		order_by = limiterDict["order_by"]
		order = limiterDict["order"]
		limit_min = limiterDict["limit_min"]
		limit_max = limiterDict["limit_max"]
		
		import json

		with open(appName+'_config.json') as json_file1:
			connDict = json.load(json_file1)
		
		with open(dbTable+'.json') as json_file:
			tableConfigs = json.load(json_file)
		
		for q in tableConfigs['columns']:
			sql = sql+q["name"]+","
		
		if not whereJSON or whereJSON=="":
			whereDict = {}
		else:
			whereDict = whereJSON
		
		if not environx or environx=="":
			environ = ""
		else:
			environ = environx
		
		qry2 = " WHERE APIKey = '"+str(APIKey)+"' "
		qry = ""
		
		for a in range(len(whereDict)):
			dict = whereDict[a]
			
			if dict["value2"]=="" or not dict["value2"]:
				qry = self.queryBuilder(qry,dict["next_field_logic"],dict["column"],dict["value"],"","")
			else:
				qry = queryBuilder(db,qry,dict["next_field_logic"],dict["column"],dict["value"],dict["value2"],dict["pre_bracket"],dict["post_bracket"])
		
		if qry==")" or qry=="" or not qry:
			qry = ""
		else:
			qry2 = qry2+" AND ("
		
		eoq = qry2+qry+" ORDER BY "+order_by+" "+order+" LIMIT "+str(limit_min)+","+str(limit_max)
		
		sql = "SELECT ID,"
		for p in tableConfigs['columns']:
			sql = sql+p["name"]+","
		
		sql = sql+"transaction_by,dateset FROM "+dbTable+" "+eoq+""
		conn = psycopg2.connect(host=connDict["host"],database=connDict["database"+environ],user=connDict["user"],password=connDict["password"])
		cur = conn.cursor()
		cur.execute(sql)
		output = cur.fetchall()
		cur.close()
		return output
 
	def add(self,id):
		return self.members
 
	def edit(self,id):
		return self.members[int(id)]
 
	def delete(self,id):
		return self.members[int(id)]
 