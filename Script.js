class WordNode {
    constructor(word) {
        this.word = word;
        this.frequency = 1;
        this.next = null;
    }
}

class WordFrequencyList {
    constructor() {
        this.head = null;
    }

    addWord(word) {
        if (!this.head) {
            this.head = new WordNode(word);
            return;
        }

        let current = this.head;
        while (current) {
            if (current.word.toLowerCase() === word.toLowerCase()) {
                current.frequency++;
                return;
            }
            if (!current.next) break;
            current = current.next;
        }

        current.next = new WordNode(word);
    }

    printWordFrequencies() {
        let current = this.head;
        while (current) {
            console.log(`${capitalize(current.word)}: ${current.frequency}`);
            current = current.next;
        }
    }
}

function capitalize(word) {
    return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
}

function main() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question('Enter text: ', (inputText) => {
        const words = inputText.split(/\s+/).filter(word => word.length > 0);

        const wordList = new WordFrequencyList();
        words.forEach(word => wordList.addWord(word));

        wordList.printWordFrequencies();
        rl.close();
    });
}

main();
