class Node {
    constructor(song) {
        this.data = song;
        this.prev = null;
        this.next = null;
    }
}

class Playlist {
    constructor() {
        this.head = null;
        this.tail = null;
        this.current = null;
    }

    addSong(song) {
        const newNode = new Node(song);
        if (!this.head) {
            this.head = this.tail = this.current = newNode;
        } else {
            this.tail.next = newNode;
            newNode.prev = this.tail;
            this.tail = newNode;
        }
    }

    removeSong(song) {
        let temp = this.head;
        while (temp) {
            if (temp.data === song) {
                if (temp.prev) temp.prev.next = temp.next;
                if (temp.next) temp.next.prev = temp.prev;
                if (temp === this.head) this.head = temp.next;
                if (temp === this.tail) this.tail = temp.prev;
                if (temp === this.current) this.current = temp.next || temp.prev;
                return;
            }
            temp = temp.next;
        }
    }

    previousSong() {
        if (this.current && this.current.prev) {
            this.current = this.current.prev;
            console.log(`Current song: ${this.current.data}`);
        } else {
            console.log("Already at the first song.");
        }
    }

    nextSong() {
        if (this.current && this.current.next) {
            this.current = this.current.next;
            console.log(`Current song: ${this.current.data}`);
        } else {
            console.log("Already at the last song.");
        }
    }

    printPlaylist() {
        let temp = this.head;
        let result = [];
        while (temp) {
            result.push(temp.data);
            temp = temp.next;
        }
        console.log(result.join(" -> "));
    }

    reversePlaylist() {
        let temp = null;
        let current = this.head;
        while (current) {
            temp = current.prev;
            current.prev = current.next;
            current.next = temp;
            current = current.prev;
        }
        if (temp) {
            this.head = temp.prev;
        }
        [this.head, this.tail] = [this.tail, this.head];
    }
}


const playlist = new Playlist();
playlist.addSong("Song 1");
playlist.addSong("Song 2");
playlist.addSong("Song 3");
playlist.printPlaylist();
playlist.nextSong();
playlist.nextSong();
playlist.previousSong();
playlist.removeSong("Song 2");
playlist.printPlaylist();
playlist.reversePlaylist();
playlist.printPlaylist(); 
