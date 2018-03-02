

export class Stats {

    /* Takes basic stats values as provided by Django
     * and turns them into stats as required to build
     * a stats progress chart or other stats summary
     *
     */

    constructor (data) {
        this.data = data;
    }

    get approvedPercent() {
        if (this.translatedStrings === 0 || this.totalStrings === 0) {
            return 0;
        }
        return parseInt(
            Math.floor(
                this.translatedStrings
                    / parseFloat(this.totalStrings) * 100));
    }

    get fuzzyShare () {
        return this._share(this.fuzzyStrings);
    }

    get fuzzyStrings () {
        return this.data ? this.data.fuzzy_strings || 0 : 0;
    }

    get missingShare () {
        if (this.totalStrings === 0) {
            return 0;
        }
        return this._share(this.missingStrings);
    }

    get missingStrings () {
        return (
            this.totalStrings
                - this.translatedStrings
                - this.fuzzyStrings
                - this.suggestedStrings);
    }

    get suggestedShare () {
        return this._share(this.suggestedStrings);
    }

    get suggestedStrings () {
        return this.data && this.data.translated_strings || 0 ? this.data.translated_strings : 0;
    }

    get totalStrings () {
        return this.data && this.data.total_strings || 0 ? this.data.total_strings : 0;
    }

    get translatedShare () {
        return this._share(this.translatedStrings);
    }

    get translatedStrings () {
        return this.data && this.data.approved_strings ? this.data.approved_strings : 0;
    }

    _share (item) {
        if (item === 0 || this.totalStrings === 0) {
            return 0;
        }
        return Math.round(item / parseFloat(this.totalStrings) * 100);
    }
}


export class AggregateStats extends Stats {

    _aggregate(accessor) {
        return this.data.map(x => x[accessor]).reduce((_s, x) => _s + x);
    }

    get fuzzyStrings () {
        return this._fuzzy = !this._fuzzy ? this._aggregate('fuzzy_strings') : this._fuzzy;
    }

    get suggestedStrings () {
        return this._suggested = !this._suggested ? this._aggregate('translated_strings') : this._suggested;
    }

    get totalStrings () {
        return this._total = !this._total ? this._aggregate('total_strings') : this._total;
    }

    get translatedStrings () {
        return this._translated = !this._translated ? this._aggregate('approved_strings') : this._translated;
    }
}