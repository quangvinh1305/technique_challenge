<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt=" Logo"
          class="shrink mr-2"
          contain
          src="https://blog.firmsone.com/content/images/size/w100/2019/06/Free_Sample_By_Wix.jpeg"
          transition="scale-transition"
          width="40"
        />
        Techinique Challenge
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://blog.firmsone.com/"
        target="_blank"
        text
      >
        <span class="mr-2">My Blog</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-content>
      <Histograms/>
    </v-content>
  </v-app>
</template>

<script>
import Histograms from './components/Histograms';

export default {
  name: 'App',

  components: {
    Histograms,
  },

  data: () => ({
    //
  }),
};
</script>
