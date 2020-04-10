<template>
  <div class="relation-wrapper">
  
  </div>
</template>

<script>

export default {
  name: 'Relation',
  data () {
    return {
      relation: null
    }
  },
  mounted () {
    this.getRelation()
  },
  methods: {
    getRelation () {
      this.$http.get(`http://127.0.0.1:5000/databases/${this.$router.currentRoute.params.dbname}/schema/${this.$router.currentRoute.params.dbschema}/tables/${this.$router.currentRoute.params.relation}`)
      .then(function (response) {
        this.relation = response.body
        console.log('this.relation', this.relation)
      }.bind(this))
      .catch(function(reject) {
        console.log('Error in getRelation, reject', reject)
      })
    }
  }
}
</script>
