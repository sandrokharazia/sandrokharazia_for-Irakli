class DocumentVersion {
    constructor(content) {
        this.content = content;
        this.next = null; // Pointer to the previous version
    }
}

class DocumentHistory {
    constructor() {
        this.head = null; // Latest version
        this.length = 0;
    }

    saveVersion(content) {
        const newVersion = new DocumentVersion(content);
        newVersion.next = this.head; // Point new version to the previous version
        this.head = newVersion; // Update head to new version
        this.length++;
        console.log("Document version saved.");
    }

    revert() {
        if (!this.head) {
            console.log("No previous version to revert to.");
            return;
        }
        this.head = this.head.next; // Move head to previous version
        this.length--;
        console.log("Reverted to the previous version.");
    }

    showCurrentVersion() {
        if (!this.head) {
            console.log("No document versions available.");
        } else {
            console.log(`Current Version:\n${this.head.content}`);
        }
    }

    showAllVersions() {
        if (!this.head) {
            console.log("No document versions available.");
            return;
        }

        console.log("All Document Versions:");
        let current = this.head;
        let versionNumber = this.length;
        while (current) {
            console.log(`Version ${versionNumber}:\n${current.content}\n`);
            current = current.next;
            versionNumber--;
        }
    }

    showListLength() {
        console.log(`Total Versions: ${this.length}`);
    }
}

// Example Usage
const docHistory = new DocumentHistory();
docHistory.saveVersion("Version 1: Initial draft.");
docHistory.saveVersion("Version 2: Added introduction.");
docHistory.saveVersion("Version 3: Fixed typos.");

docHistory.showCurrentVersion();
docHistory.showListLength();
docHistory.showAllVersions();

docHistory.revert();
docHistory.showCurrentVersion();
docHistory.showListLength();

