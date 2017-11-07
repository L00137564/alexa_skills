//var cmd = require ('gulp-run');
var cmd = require('node-cmd');

////////////////////////////////////////////////////////////////
function sleep (time) {
    return new Promise((resolve) => setTimeout(resolve, time));
}
////////////////////////////////////////////////////////////////

console.log('Starting directory: ' + process.cwd());

var listSkills = 'ask api list-skills -p owen'

cmd.get( listSkills,
    function(err, data, stderr){
        console.log('the current working dir is : ',data)
        }
    );
