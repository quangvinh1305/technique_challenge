<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          src="https://blog.firmsone.com/content/images/size/w100/2019/06/Free_Sample_By_Wix.jpeg"
          class="my-3"
          contain
          height="200"
        />
      </v-col>

      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">
          Welcome to Technique Challenge
        </h1>

        <p class="subheading font-weight-regular">
          If you need help to preview this techinique challenge,
          <br>please contact me
          <a
            href="mailto:quangvinh.13@gmail.com"
          >My Email Address</a>
        </p>
      </v-col>

    </v-row>
    <v-row class="text-center">
      <v-col cols="12">
        <v-text-field placeholder="Enter Your Url Here" v-model='url' @input="histogramsForUrl"></v-text-field>
      </v-col>
      <v-col cols="12">
        <BarChart :dataSets="dataSets" v-if="dataSets.data" />
      </v-col>

    </v-row>
  </v-container>
</template>

<script>
  import Vue from 'vue'
  import BarChart from './BarChart'
  export default {
    name: 'Histograms',
    components: {BarChart},
    async mounted() {
    },
    async created(){
      this.histogramsForUrl();
    },
    methods: {
      async histogramsForUrl(){
        let res = await Vue.axios.get(`http://127.0.0.1:8000/api/histograms?url=${this.url}`);
        if(res.data){
          this.dataSets = {}
          Vue.set(this.dataSets, 'labels', Object.keys(res.data));
          Vue.set(this.dataSets, 'data', Object.values(res.data));
          this.dataSets.label = "Histograms";
        }
      },
    },
    data: () => ({
      url: 'https://apps.apple.com/vn/app/elsa-speak-accent-reduction/id1083804886',
      dataSets: {},
      ecosystem: [
      ],
      importantLinks: [

      ],
      whatsNext: [
      ],
    }),
  }
</script>
