<template>
  <div class="databases-wrapper">
    <b-table :data="databases" :columns="columns">
      <template slot-scope="props">
        <b-table-column>
          <router-link :to="{ name: 'database_tables', params: { dbname: props.row.datname }}">
            {{ props.row.datname }}
          </router-link>
        </b-table-column>
      </template>
    </b-table>
  </div>
</template>

<script>

export default {
  name: 'Databases',
  data () {
    return {
      databases: [],
      columns: [
        {
          field: 'datname',
          label: 'Databases',
        },
      ]
    }
  },
  mounted () {
    this.getDataBases()
  },
  methods: {
    getDataBases () {
      this.$http.get('http://127.0.0.1:5000/databases')
      .then(function (response) {
        this.databases = response.body
      }.bind(this))
      .catch(function(reject) {
        console.log('Error in getDataBases, reject', reject)
      })
    }
  }
}
</script>
