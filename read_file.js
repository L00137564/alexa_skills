var file_path = 'C:\\Users\\x213859\\.jenkins\\workspace\\alexa_skills_test_scripts\\latest_modified_skill.txt'

function read_from_file(file){
    var fs = require('fs');
    fs.readFile(file, 'utf8', function(err, data) {  
        if (err) throw err;
        console.log(data);
    });
}

read_from_file(file_path);