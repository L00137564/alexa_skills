//var cmd = require ('gulp-run');
var cmd = require('node-cmd');

console.log('Starting directory: ' + process.cwd());

var skillName = 'test_skill_501'
var deploy = 'ask deploy -t skill -p owen'

process.chdir('C:\\Users\\x213859\\.jenkins\\workspace\\alexa_pipeline_demo\\' + skillName)


cmd.get( deploy,
    function(err, data, stderr){
        console.log('the current working dir is : ',data)
        }
    );
