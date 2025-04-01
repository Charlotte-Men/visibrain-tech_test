<template>
  <GameForm @videos-found="fetchVideos" />
  <div>
    <div>{{ videos.length }}</div>
    <div v-for="video in videos">
      {{ video.title }} - {{ video.user_name }}
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import GameForm from "./GameForm.vue";
import { fetchVideosByGame } from "../services/api";

export default {
  components: { GameForm },
  setup() {
    const videos = ref([]);

    const fetchVideos = async (gameName) => {
      const result = await fetchVideosByGame(gameName);
      if (result.Videos) {
        console.log(result)
        videos.value = result.Videos;
      }
    };
    console.log(videos.value)
    return { videos, fetchVideos };
  },
};
</script>
