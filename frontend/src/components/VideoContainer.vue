<template>
  <GameForm @videos-found="fetchVideos" />
  <div class="videos-list">
    <VideoInfos v-for="video in videos" :key="video.id" :video="video" />
  </div>
</template>

<script>
import { ref, onMounted, onUnmounted } from "vue";
import GameForm from "./GameForm.vue";
import VideoInfos from "./VideoInfos.vue";
import { fetchVideosByGame } from "../services/api";

export default {
  components: { GameForm, VideoInfos },
  setup() {
    const videos = ref([]);
    const currentGameName = ref("");
    let intervalId = null;

    const fetchVideos = async (gameName) => {
      // Save game name for video refresh
      if (gameName) currentGameName.value = gameName;

      const result = await fetchVideosByGame(gameName);
      if (result.Videos) {
        videos.value = result.Videos;
      }
    };

    // Refresh videos every 2min
    onMounted(() => {
      intervalId = setInterval(() => {
        if (currentGameName.value) fetchVideos(currentGameName.value);
      }, 120000);
    });

    // Clear timer on component unmount
    onUnmounted(() => {
      clearInterval(intervalId);
    });

    return { videos, fetchVideos };
  },
};
</script>
