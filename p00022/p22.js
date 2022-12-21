

const fs = require('fs');

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
letter_score = 0;
ls = {}
for (i in letters) {
    letter_score+=1;
    ls[letters[i]] = letter_score;
}
  
fs.readFile('names.txt', (err, data) => {
    if (err) throw err;
    name_list = data.toString().split(',').sort();

    order = 0;
    score = 0;
    for (i in name_list) {
        order += 1
        item_name = name_list[i].slice(1, -1);
        name_score = 0;
        for (j in item_name) {
            name_score += ls[item_name[j]];
        }
        name_score *= order;
        score+=name_score;
    }
    console.log(score)
})

