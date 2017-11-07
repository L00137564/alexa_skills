var fs = require('fs')

var out_file = "C:\\Users\\x213859\\.jenkins\\workspace\\alexa_skills_test_scripts\\js_write.txt"
var string = "Hey there!"

function write_to_file(file, str){
    fs.writeFile(file, str, function(err) {
        if(err) {
            return console.log(err);
        }
        console.log("Write successful");
    }); 
}

write_to_file(out_file, string);
