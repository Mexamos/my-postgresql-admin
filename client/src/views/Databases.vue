<template>
  <div class="home">
  </div>
</template>

<script>

export default {
  name: 'Databases',
  mounted () {
    this.getDataBases()
  },
  methods: {
    getDataBases () {
      this.$http.get('http://127.0.0.1:5000/databases')
      .then(function (response) {
        console.log('response', response)
      })
    }
  }
}
</script>
