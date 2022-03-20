const csv = require('csv-parser');
const fs = require('fs')

const fileArray = fs.readdirSync('./data')
let sum =0
let highest = -1
let lowest = 99999
let count =0


fs.createReadStream('./data/20220314-0705.csv')
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
    console.log('Average karma: ' + parseInt(sum/count))
    console.log('Highest: ' + highest)
    console.log('Lowest: ' + lowest)
    });