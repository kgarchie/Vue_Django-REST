<template>
  <div className="home">
    <section className="hero is-medium is-dark mb-6">
      <div className="hero-body has-text-centered">
        <p className="title mb-6">
          Welcome to App
        </p>
        <p className="subtitle">
          The best shop online
        </p>
      </div>
    </section>

    <div className="columns is-multiline">
      <div className="column is-12">
        <h2 className="is-size-2 has-text-centered">Latest Products</h2>
      </div>

      <div className="column is-3" v-for="product in latestProducts" v-bind:key="product.id">
        <div className="box">
          <figure className="image mb-4">
            <img v-bind:src="product.get_thumbnail" alt="">
          </figure>
        </div>
        <h3 className="is-size-4">{{ product.name }}</h3>
        <p className="is-size-6 has-text-grey">KES{{ product.price }}</p>

        <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4">View Details</router-link>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      latestProducts: []
    }
  },
  components: {},
  mounted() {
    this.getLatestProducts()
  },
  methods: {
    getLatestProducts() {
      axios.get('/api/v1/latest-products/').then(response => {
        this.latestProducts = response.data
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>
<style scoped>
.image {
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
}
</style>
