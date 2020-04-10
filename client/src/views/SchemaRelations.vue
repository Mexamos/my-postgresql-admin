<template>
  <div class="scheme-wrapper">
    <div class="relations">
      <div class="relation-wrapper" v-if="relations && relations.length > 0" @click="$router.push({ name: 'relation', params: { dbname: $router.currentRoute.params.dbname, dbschema: $router.currentRoute.params.dbschema, relation: relation.table_name }})" v-for="(relation, index) in relations" :key="index">
        <div class="relation-title">
          Relation name: {{ relation.table_name }}
        </div>
        <div class="relation-title">
          Relation type: {{ relation.table_type }}
        </div>

        <relation-view :relation="relation.columns"></relation-view>
      </div>
    </div>
  </div>
</template>

<script>
import RelationView from '@/components/RelationView.vue'

export default {
  name: 'SchemaRelations',
  components: {
    RelationView
  },
  data () {
    return {
      relations: [],
    }
  },
  mounted () {
    this.getSchema()
  },
  methods: {
    getSchema () {
      this.$http.get(`http://127.0.0.1:5000/databases/${this.$router.currentRoute.params.dbname}/schema/${this.$router.currentRoute.params.dbschema}`)
      .then(function (response) {
        this.relations = response.body
      }.bind(this))
      .catch(function(reject) {
        console.log('Error in getDataBaseTables, reject', reject)
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.scheme-wrapper {

  .relations {
    display: flex;
    flex-wrap: wrap;

    .relation-wrapper {
      border: 1px solid grey;
      border-radius: 3px;
      padding: 10px;
      margin: 20px;
      min-width: 300px;
      cursor: pointer;

      .relation-title {
        text-align: left;
        margin-bottom: 3px;
      }
    }
    .relation-wrapper:hover {
      box-shadow: 0 0 10px rgba(0,0,0,0.5);
      transition: .3s;
    }
  }
}
</style>
