from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from blog.models import Post
from accounts.models import CustomUser
from core.models import Category


class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        cls.category = Category.objects.create(
            name="Django"
        )

        cls.thumbnail = SimpleUploadedFile(
            name="test.jpg",
            content=b"fake image content",
            content_type="image/jpeg"
        )

        cls.post = Post.objects.create(
            title="Test Post",
            summary="Test Summary",
            description="Test Description",
            thumbnail=cls.thumbnail,
            author=cls.user,
        )

        cls.post.categories.add(cls.category)

    def test_post_creation(self):
        self.assertIsInstance(self.post, Post)
        self.assertEqual(Post.objects.count(), 1)

    def test_post_str(self):
        self.assertEqual(str(self.post), "Test Post")

    def test_post_title(self):
        self.assertEqual(self.post.title, "Test Post")

    def test_post_summary(self):
        self.assertEqual(self.post.summary, "Test Summary")

    def test_post_description(self):
        self.assertEqual(self.post.description, "Test Description")

    def test_post_is_active_default(self):
        self.assertTrue(self.post.is_active)

    def test_post_author(self):
        self.assertEqual(self.post.author, self.user)

    def test_post_category(self):
        self.assertIn(self.category, self.post.categories.all())

    def test_post_get_absolute_url(self):
        expected_url = reverse(
            "blog:post-detail",
            kwargs={"pk": self.post.id}
        )

        self.assertEqual(
            self.post.get_absolute_url(),
            expected_url
        )

    def test_post_write_at(self):
        self.assertIsNotNone(self.post.write_at)

    def test_post_update_at(self):
        self.assertIsNotNone(self.post.update_at)