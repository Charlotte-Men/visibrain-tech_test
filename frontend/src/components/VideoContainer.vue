<template>
  <GameForm @videos-found="fetchVideos" />
  <p v-if="videos.length">
    {{ videos.length }} videos found (refreshing results in {{ countdown }}s)
  </p>
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
    const countdown = ref(120);
    let intervalId = null;
    let countdownId = null;

    const fetchVideos = async (gameName) => {
      // Save game name for video refresh
      if (gameName) currentGameName.value = gameName;

      const result = await fetchVideosByGame(gameName);
      if (result.Videos) {
        videos.value = result.Videos;
      }

      // Reset countdown after an API call
      countdown.value = 120;
    };

    onMounted(() => {
      // Decrement countdown every second
      countdownId = setInterval(() => {
        if (countdown.value > 0) {
          countdown.value--;
        }
      }, 1000);
      
      // Refresh videos every 2min
      intervalId = setInterval(() => {
        if (currentGameName.value) fetchVideos(currentGameName.value);
      }, 120000);
    });

    // Clear countdown on component unmount
    onUnmounted(() => {
      clearInterval(intervalId);
      clearInterval(countdownId);
    });

    return { videos, fetchVideos, countdown };
  },
};
</script>
