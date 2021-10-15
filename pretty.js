var fs = require('fs');

/* 참고로만.. 어떻게 json prettier하는지 확인 
*/

fs.readFile("./getnames.json", "utf8", (err, jsonString) => {
	if (err) {
	  console.log("Error reading file from disk:", err);
	  return;
	}
	try {
		parsed = JSON.parse(jsonString)
		fs.writeFile('getnames.json', JSON.stringify(parsed, null, 2), err => {
			if (err) console.log(err);
		});
		lenn = (Object.keys(parsed.data).length);
		console.log(parsed.data[3]["company_name"]);
		
		for (let i = 0; i < lenn; i++){
			fs.writeFile('names.txt', parsed.data[i]["company_name"] + '\n', err => {
				if (err) console.log(err);
			})
		}

	} catch (err) {
	  console.log("Error parsing JSON string:", err);
	}
	return ;
  });