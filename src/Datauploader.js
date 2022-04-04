const fs = require('fs');
const csv = require('csv-parser');
const { exit } = require('process');

const fileArray = fs.readdirSync('./raw_data')
const arr = [1]
let post_ids = []



arr.forEach(fileName => {
    //currentFile = './raw_data/'+fileName;
    let currentFile = '../20220314-0935.csv'
    let timestamp = currentFile.slice(3,-4);

    fs.createReadStream(currentFile)
        .pipe(csv())
        .on('data', (data) =>{
            post_id = data.id;
            post_title = data.title;
            post_author = data.author;
            post_score = data.score;
            post_sub = data.subreddit;
            post_comments= data.num_comments;
            post_link = data.permalink;
            post_isNSFW = data.over_18;
            let JSONobject = {
                id : post_id,
                details : {
                    title : post_title,
                    author : post_author,
                    subreddit: post_sub,
                    link : post_link,
                    isNSFW : post_isNSFW,
                    score : {post_score},
                    num_comments : {post_comments}
                }
            }
            console.log(JSONobject.details.score.post_score);
            
        })
        .on('end', () => {
            ;
        })

});