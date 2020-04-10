<template>
  <div class="databases-wrapper">
    <b-table :data="tables" :columns="columns">
      <template slot-scope="props">
        <b-table-column>
          <router-link :to="{ name: 'schema_relations', params: { dbname: $router.currentRoute.params.dbname, dbschema: props.row.table_schema }}">
            {{ props.row.table_schema }}
          </router-link>
        </b-table-column>

        <b-table-column>
          <router-link :to="{ name: 'relation', params: { dbname: $router.currentRoute.params.dbname, dbschema: props.row.table_schema, relation: props.row.table_name }}">
            {{ props.row.table_name }}
          </router-link>
        </b-table-column>

        <b-table-column>
          {{ props.row.table_type }}
        </b-table-column>
      </template>
    </b-table>
  </div>
</template>

<script>

export default {
  name: 'DatabaseRelations',
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
    this.getDataBaseTables()
  },
  methods: {
    getDataBaseTables () {
      this.$http.get(`http://127.0.0.1:5000/databases/${this.$router.currentRoute.params.dbname}/tables`)
      .then(function (response) {
        this.tables = response.body
      }.bind(this))
      .catch(function(reject) {
        console.log('Error in getDataBaseTables, reject', reject)
      })
    }
  }
}
</script>
