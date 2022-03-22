const csv = require('csv-parser');
const fs = require('fs');

const fileArray = fs.readdirSync('./raw_data')

fileArray.forEach(fileName => {
    
    let sum =0
    let highest = -1
    let lowest = 999999
    let count =0

    currentFile = './raw_data/'+fileName;

    fs.createReadStream(currentFile)
        .pipe(csv())
        .on('data', (row) => {
        sum = sum + parseInt(row.score)
        count+=1;
        if(parseInt(row.score) > highest){
            highest = parseInt(row.score)
        }

        if(parseInt(row.score) < lowest)
            lowest = parseInt(row.score)
        })
        .on('end', () => {
            console.log("File inormation for: " + fileName)
            console.log('Average karma: ' + parseInt(sum/count))
            console.log('Highest: ' + highest)
            console.log('Lowest: ' + lowest)
            console.log('\n')
        });
});