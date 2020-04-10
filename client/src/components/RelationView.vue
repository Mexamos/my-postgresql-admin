<template>
  <div v-if="relation">
    <b-table :data="relation" :columns="columns">
      <template slot-scope="props">
        <b-table-column>
          {{ props.row.column_name }}
        </b-table-column>

        <b-table-column>
          {{ props.row.data_type }}
        </b-table-column>
      </template>
    </b-table>
  </div>
</template>

<script>
export default {
  name: 'RelationView',
  props: [
    'relation'
  ],
  data () {
    return {
      columns: [
        {
          field: 'column_name',
          label: 'Column name',
        },
        {
          field: 'data_type',
          label: 'Type',
        },
      ]
    }
  }
}
</script>

<style lang="scss" scoped>

</style>