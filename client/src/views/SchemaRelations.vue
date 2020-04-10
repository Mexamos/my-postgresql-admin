<template>
  <div class="databases-wrapper">
    <!-- <b-table :data="tables" :columns="columns">
      <template slot-scope="props">
        <b-table-column>
          <router-link :to="{ name: 'database_tables', params: { dbname: props.row.table_schema }}">
            {{ props.row.table_schema }}
          </router-link>
        </b-table-column>

        <b-table-column>
          <router-link :to="{ name: 'database_tables', params: { dbname: props.row.table_name }}">
            {{ props.row.table_name }}
          </router-link>
        </b-table-column>

        <b-table-column>
          {{ props.row.table_type }}
        </b-table-column>
      </template>
    </b-table> -->
  </div>
</template>

<script>

export default {
  name: 'SchemaRelations',
  data () {
    return {
      tables: [],
      columns: [
        {
          field: 'table_schema',
          label: 'Schema',
        },
        {
          field: 'table_name',
          label: 'Table name',
        },
        {
          field: 'table_type',
          label: 'Table type',
        },
      ]
    }
  },
  mounted () {
    this.getSchema()
  },
  methods: {
    getSchema () {
      this.$http.get(`http://127.0.0.1:5000/databases/${this.$router.currentRoute.params.dbname}/schema/${this.$router.currentRoute.params.dbschema}`)
      .then(function (response) {
        console.log('response', response)
      }.bind(this))
      .catch(function(reject) {
        console.log('Error in getDataBaseTables, reject', reject)
      })
    }
  }
}
</script>
