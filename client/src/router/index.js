import Vue from 'vue'
import VueRouter from 'vue-router'
import Databases from '../views/Databases.vue'
import DatabaseRelations from '../views/DatabaseRelations.vue'
import SchemaRelations from '../views/SchemaRelations.vue'
import Relation from '../views/Relation.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'databases',
    component: Databases
  },
  {
    path: '/:dbname/tables',
    name: 'database_tables',
    component: DatabaseRelations
  },
  {
    path: '/:dbname/schema/:dbschema',
    name: 'schema_relations',
    component: SchemaRelations
  },
  {
    path: '/:dbname/schema/:dbschema/relation/:relation',
    name: 'relation',
    component: Relation
  },
]

const router = new VueRouter({
  routes
})

export default router
